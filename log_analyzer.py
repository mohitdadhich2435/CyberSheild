"""Transparent rule-based analyzer for sample logs; not a production IDS."""
import re
from collections import Counter

FAILED_PATTERNS = [
    re.compile(r"failed password", re.I),
    re.compile(r"login failed", re.I),
    re.compile(r"authentication failure", re.I),
    re.compile(r"invalid user", re.I),
]

def analyze_log_text(text: str) -> list[dict]:
    lines = text.splitlines()
    failed = [line for line in lines if any(p.search(line) for p in FAILED_PATTERNS)]
    alerts = []
    if len(failed) >= 5:
        alerts.append({
            "severity": "High",
            "title": "Repeated authentication failures",
            "count": len(failed),
            "recommendation": "Verify whether the activity is expected; review source IPs and authentication logs."
        })
    elif failed:
        alerts.append({
            "severity": "Medium",
            "title": "Authentication failures observed",
            "count": len(failed),
            "recommendation": "Review the events and correlate them with user and source-IP context."
        })
    suspicious = [line for line in lines if re.search(r"(powershell.*-enc|known malicious|eicar)", line, re.I)]
    if suspicious:
        alerts.append({
            "severity": "High",
            "title": "Potentially suspicious command or test signature",
            "count": len(suspicious),
            "recommendation": "Validate these events in an isolated lab and follow your incident-response process."
        })
    if not alerts:
        alerts.append({
            "severity": "Info",
            "title": "No configured rule triggered",
            "count": 0,
            "recommendation": "This does not prove the logs are benign; add rules and correlate with other telemetry."
        })
    return alerts
