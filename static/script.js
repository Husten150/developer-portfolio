const $ = (s) => document.querySelector(s);
function esc(v) {
  return String(v).replace(/[&<>"']/g, (c) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  })[c]);
}
function githubUrl(v) {
  try {
    const u = new URL(v);
    return u.protocol === "https:" && u.hostname === "github.com" ? u.href : "#";
  } catch { return "#"; }
}
async function health() {
  try {
    const r = await fetch("/api/health");
    const d = await r.json();
    $("#api-status").textContent = d.status === "ok" ? "Online" : "Unavailable";
  } catch { $("#api-status").textContent = "Offline"; }
}
async function projects() {
  try {
    const r = await fetch("/api/projects");
    if (!r.ok) throw new Error("Request failed");
    const d = await r.json();
    $("#project-list").innerHTML = d.projects.map((p) =>
      '<article class="project"><small>' + esc(p.category) + '</small><h3>' +
      esc(p.name) + '</h3><p>' + esc(p.description) +
      '</p><a target="_blank" rel="noopener noreferrer" href="' +
      esc(githubUrl(p.github_url)) + '">Explore repository ↗</a></article>'
    ).join("");
  } catch { $("#project-list").textContent = "Could not load projects. Refresh to try again."; }
}
async function run() {
  const b = $("#run-request");
  b.disabled = true;
  $("#response-status").textContent = "Loading…";
  try {
    const r = await fetch($("#endpoint").value);
    const d = await r.json();
    $("#response-status").textContent = r.status + " " + r.statusText;
    $("#api-response").textContent = JSON.stringify(d, null, 2);
  } catch (e) {
    $("#response-status").textContent = "Request failed";
    $("#api-response").textContent = e.message;
  } finally { b.disabled = false; }
}
document.addEventListener("DOMContentLoaded", () => {
  $("#year").textContent = new Date().getFullYear();
  $("#run-request").addEventListener("click", run);
  health();
  projects();
});
