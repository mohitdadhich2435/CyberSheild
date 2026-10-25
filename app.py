from flask import Flask, render_template, request, jsonify
from scanner import check_security_headers
from log_analyzer import analyze_log_text
import os

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/api/scan")
def scan():
    data = request.get_json(silent=True) or {}
    target = (data.get("url") or "").strip()
    # MVP safety guard: only allow explicitly authorized public HTTP(S) targets.
    if not target.startswith(("https://", "http://")):
        return jsonify({"error": "Enter a valid http:// or https:// URL."}), 400
    result = check_security_headers(target)
    return jsonify(result)

@app.post("/api/analyze-logs")
def analyze_logs():
    data = request.get_json(silent=True) or {}
    text = data.get("logs", "")
    if not isinstance(text, str) or len(text) > 200_000:
        return jsonify({"error": "Provide log text under 200 KB."}), 400
    return jsonify({"alerts": analyze_log_text(text)})

if __name__ == "__main__":
    app.run(debug=True)
