"""Basic security-header checker for authorized targets only."""
import requests
from urllib.parse import urlparse

HEADERS_TO_CHECK = {
    "Content-Security-Policy": "Helps reduce script-injection and content-loading risks.",
    "Strict-Transport-Security": "Encourages browsers to use HTTPS.",
    "X-Content-Type-Options": "Helps prevent MIME-type sniffing.",
    "X-Frame-Options": "Helps reduce clickjacking risk.",
    "Referrer-Policy": "Controls referrer information sent by the browser.",
    "Permissions-Policy": "Restricts access to selected browser features.",
}

def check_security_headers(url: str) -> dict:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        return {"url": url, "error": "Invalid URL.", "findings": []}
    try:
        response = requests.get(
            url, timeout=8, allow_redirects=True,
            headers={"User-Agent": "CyberShield-Lab/1.0"}
        )
        present = {k.lower(): v for k, v in response.headers.items()}
        findings = []
        for header, explanation in HEADERS_TO_CHECK.items():
            value = present.get(header.lower())
            findings.append({
                "header": header,
                "status": "Present" if value else "Missing",
                "detail": value if value else explanation,
                "severity": "Info" if value else "Review"
            })
        return {
            "url": url,
            "final_url": response.url,
            "status_code": response.status_code,
            "findings": findings
        }
    except requests.RequestException as exc:
        return {"url": url, "error": f"Request failed: {exc}", "findings": []}
