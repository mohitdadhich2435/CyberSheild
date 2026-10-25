# CyberShield

CyberShield is an educational cybersecurity operations dashboard built with Python and Flask. The MVP provides a passive HTTP security-header audit for authorized targets and a transparent, rule-based analyzer for sample authentication logs.

## Features

- Dark security operations dashboard
- HTTP security-header checks
- Rule-based triage for repeated authentication failures and selected suspicious log patterns
- JSON endpoints for extending the project
- No exploit execution or automated endpoint isolation

## Requirements

- Python 3.10+
- pip

## Run locally

```bash
python -m venv .venv
```

Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install and run:
```bash
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Use responsibly

Only scan systems you own or have explicit authorization to assess. This is a learning prototype, not a production security scanner. Header presence does not prove a site is secure, and missing headers are not always vulnerabilities in every context. Log rules are illustrative and can produce false positives/negatives.

## Roadmap

1. Add persistent findings storage and downloadable reports.
2. Add unit tests and structured logging.
3. Integrate OWASP ZAP in a controlled test environment.
4. Add a Wazuh integration for alert ingestion.
5. Train/evaluate an anomaly classifier using a public dataset.
6. Add cloud posture checks with Checkov/Terraform.
7. Add CI checks with GitHub Actions, Trivy, and SonarQube.

## Project structure

```text
CyberShield/
├── app.py
├── scanner.py
├── log_analyzer.py
├── requirements.txt
├── README.md
├── PROJECT_REPORT.md
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── app.js
```
