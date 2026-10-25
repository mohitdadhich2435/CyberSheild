# CyberShield — Project Report

## 1. Abstract
CyberShield is an educational security operations prototype that brings together basic web security-header auditing and rule-based log triage in one dashboard. It demonstrates how small, modular tools can support security visibility and incident investigation.

## 2. Problem statement
Teams may need to review website security configuration and investigate authentication logs. Separate tools and noisy output can make these tasks harder for learners. CyberShield provides a simple interface and clear findings for two introductory workflows.

## 3. Objectives
- Check selected HTTP security headers on authorized targets.
- Identify repeated authentication failures in supplied logs.
- Explain findings with suggested follow-up actions.
- Provide a modular foundation for future SIEM, SOAR, ML, and cloud-security integrations.

## 4. Technology stack
- Python and Flask for the application and API.
- Requests for HTTP header inspection.
- HTML, CSS, and JavaScript for the interface.
- Rule-based pattern matching for sample log triage.

## 5. System design
The browser interface sends JSON requests to Flask endpoints. `/api/scan` invokes the passive header checker in `scanner.py`. `/api/analyze-logs` passes user-provided text to `log_analyzer.py`, which returns alerts based on transparent rules. The front end renders results and escapes dynamic text before displaying it.

## 6. Modules
### Web security header audit
Checks for Content-Security-Policy, Strict-Transport-Security, X-Content-Type-Options, X-Frame-Options, Referrer-Policy, and Permissions-Policy. The result describes whether each header was present in the HTTP response.

### Log threat triage
Counts common authentication-failure messages and flags selected illustrative suspicious strings. These rules are examples only and are not a full intrusion detection system.

## 7. Testing plan
- Start the application and confirm the dashboard loads.
- Run a header check against a website for which permission exists.
- Test invalid URL handling and unreachable hosts.
- Load the included sample logs and verify a repeated-failure alert appears.
- Submit empty logs and confirm the result explains that no configured rule triggered.
- Test on a local machine and avoid scanning third-party systems without permission.

## 8. Limitations
- The header checker is not a comprehensive vulnerability scanner.
- Cross-origin browser restrictions, redirects, and server behavior may affect results.
- Rule-based log triage can produce false positives and false negatives.
- No production authentication, database, role-based access control, or audit trail is included.
- Wazuh, Shuffle, ML, Active Directory, Cloudflare, Terraform, and CI/CD integrations are future work, not implemented in this MVP.

## 9. Ethical and security considerations
Use the tool only on systems you own or are explicitly authorized to assess. Do not enter secrets or sensitive logs. Keep the development server bound to localhost while testing. Before production use, add authentication, input validation, rate limiting, safe network egress controls, persistent audit logs, and security review.

## 10. Future enhancements
- Store findings and generate PDF/CSV reports.
- Integrate OWASP ZAP against a deliberately vulnerable local test application.
- Ingest alerts from Wazuh and route approved actions through a test SOAR instance.
- Evaluate a Scikit-learn anomaly detector on a public dataset with documented metrics.
- Add Checkov/Terraform cloud posture checks and GitHub Actions CI security gates.

## 11. Conclusion
CyberShield demonstrates a small, extensible foundation for security monitoring and investigation. Its key learning outcomes are modular design, safe input handling, passive web checks, basic log analysis, and clear documentation of limitations.
