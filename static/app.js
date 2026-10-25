const scanForm = document.querySelector("#scan-form");
const scanOutput = document.querySelector("#scan-output");
const logOutput = document.querySelector("#log-output");

function esc(value) {
  return String(value ?? "").replace(/[&<>"']/g, ch => ({
    "&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;", "'":"&#39;"
  })[ch]);
}

scanForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const url = document.querySelector("#url").value.trim();
  scanOutput.className = "output";
  scanOutput.textContent = "Scanning…";
  try {
    const response = await fetch("/api/scan", {
      method: "POST", headers: {"Content-Type":"application/json"},
      body: JSON.stringify({url})
    });
    const data = await response.json();
    if (!response.ok || data.error) throw new Error(data.error || "Scan failed");
    scanOutput.innerHTML = `<strong>HTTP ${esc(data.status_code)}</strong> · ${esc(data.final_url || data.url)}` +
      (data.findings || []).map(f => `<div class="finding"><span class="pill ${f.status === "Missing" ? "review" : ""}">${esc(f.status)}</span><strong>${esc(f.header)}</strong><div>${esc(f.detail)}</div></div>`).join("");
  } catch (error) {
    scanOutput.textContent = error.message || "Request failed.";
  }
});

document.querySelector("#sample").addEventListener("click", () => {
  document.querySelector("#logs").value =
`Oct 25 09:10:01 server sshd: Failed password for invalid user admin from 203.0.113.44 port 51001 ssh2
Oct 25 09:10:03 server sshd: Failed password for invalid user admin from 203.0.113.44 port 51002 ssh2
Oct 25 09:10:05 server sshd: Failed password for invalid user admin from 203.0.113.44 port 51003 ssh2
Oct 25 09:10:07 server sshd: Failed password for invalid user admin from 203.0.113.44 port 51004 ssh2
Oct 25 09:10:09 server sshd: Failed password for invalid user admin from 203.0.113.44 port 51005 ssh2`;
});

document.querySelector("#analyze").addEventListener("click", async () => {
  logOutput.className = "output";
  logOutput.textContent = "Analyzing…";
  try {
    const response = await fetch("/api/analyze-logs", {
      method: "POST", headers: {"Content-Type":"application/json"},
      body: JSON.stringify({logs: document.querySelector("#logs").value})
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || "Analysis failed");
    logOutput.innerHTML = (data.alerts || []).map(a =>
      `<div class="finding"><span class="pill ${esc(a.severity.toLowerCase())}">${esc(a.severity)}</span><strong>${esc(a.title)}</strong><div>Events: ${esc(a.count)}</div><div>${esc(a.recommendation)}</div></div>`
    ).join("");
  } catch (error) {
    logOutput.textContent = error.message || "Analysis failed.";
  }
});
