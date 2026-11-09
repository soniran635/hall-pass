with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Inject the personal Universal Relay constant right at the top of the <script> section
old_script_start = "<script>"
new_script_start = """<script>
    const UNIVERSAL_RELAY_ENDPOINT = "https://script.google.com/macros/s/AKfycbz-ZuJCLA_MT6IDW70BTq8oQ2OS7InPEdRQHKcTmDPfloL9IGv_3zHcn96qZzV3-Os1/exec";
    
    function extractGoogleSheetId(inputUrl) {
      if (!inputUrl) return "";
      const match = inputUrl.match(/\\/spreadsheets\\/d\\/([a-zA-Z0-9-_]+)/);
      if (match && match[1]) return match[1];
      if (/^[a-zA-Z0-9-_]{25,60}$/.test(inputUrl.trim()) && !inputUrl.trim().startsWith("AKfycb")) {
        return inputUrl.trim();
      }
      return "";
    }

    function getActiveEndpointAndSheetId() {
      const raw = (appState.webhookUrl || "").trim();
      if (!raw) return { endpoint: "", sheetId: "" };
      const sheetId = extractGoogleSheetId(raw);
      if (sheetId) {
        return { endpoint: UNIVERSAL_RELAY_ENDPOINT, sheetId: sheetId };
      }
      return { endpoint: raw, sheetId: "" };
    }"""

if UNIVERSAL_RELAY_ENDPOINT not in html:
    html = html.replace(old_script_start, new_script_start, 1)

# Ensure syncRostersFromGoogleSheet uses UNIVERSAL_RELAY_ENDPOINT when a Google Sheet URL is pasted
old_sync = """    async function syncRostersFromGoogleSheet() {
      saveWebhookUrl();
      const cfg = getActiveEndpointAndSheetId();
      if (!cfg.endpoint) return alert("Please paste your Google Sheet link first.");"""

new_sync = """    async function syncRostersFromGoogleSheet() {
      saveWebhookUrl();
      const cfg = getActiveEndpointAndSheetId();
      if (!cfg.endpoint && !cfg.sheetId) return alert("Please paste your Google Sheet link first.");
      
      const targetSheetId = cfg.sheetId || extractGoogleSheetId(appState.webhookUrl);
      if (!targetSheetId) {
        return alert("Please paste a valid Google Sheet URL (https://docs.google.com/spreadsheets/d/.../edit)");
      }

      showToast("Pulling rosters via Universal Engine...");
      const cb = 'roster_cb_' + Date.now();
      let handled = false;

      window[cb] = function(data) {
        handled = true;
        delete window[cb];
        if (data && data.success && data.rosters) {
          appState.rosters = data.rosters;
          localStorage.setItem('hallPassRosters', JSON.stringify(appState.rosters));
          renderTeacherRosters();
          showToast("Success! Pulled all periods & student names from Sheet.");
        } else {
          alert("Sheet Error: " + (data ? data.error : "Ensure your sheet Share setting is 'Anyone with the link -> Editor'."));
        }
      };

      const script = document.createElement('script');
      script.src = UNIVERSAL_RELAY_ENDPOINT + "?sheetId=" + encodeURIComponent(targetSheetId) + "&callback=" + cb;
      script.onerror = function() {
        if (handled) return;
        handled = true;
        delete window[cb];
        fetch(UNIVERSAL_RELAY_ENDPOINT, {
          method: "POST",
          headers: { "Content-Type": "text/plain;charset=utf-8" },
          body: JSON.stringify({ action: "GET_ROSTERS", sheetId: targetSheetId })
        }).then(r => r.json()).then(res => {
          if (res && res.success && res.rosters) {
            appState.rosters = res.rosters;
            localStorage.setItem('hallPassRosters', JSON.stringify(appState.rosters));
            renderTeacherRosters();
            showToast("Success! Pulled all periods & student names from Sheet.");
          } else {
            alert("Error: " + (res ? res.error : "Unknown error"));
          }
        }).catch((e) => {
          alert("Connection failed: " + e.message);
        });
      };
      document.body.appendChild(script);
    }"""

# Replace syncRostersFromGoogleSheet
if "async function syncRostersFromGoogleSheet()" in html:
    # Find and replace sync function
    start_idx = html.find("async function syncRostersFromGoogleSheet()")
    end_idx = html.find("function pushLogsToGoogleSheet()")
    if start_idx != -1 && end_idx != -1:
        html = html[:start_idx] + new_sync + "\n\n    " + html[end_idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully baked Universal Relay endpoint and Google Sheet URL router into index.html!")
