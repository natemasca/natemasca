# 🛡️ Ethical Web Penetration Testing: OWASP Juice Shop

## 📌 Overview
This project is an ethical web application vulnerability assessment performed on **OWASP Juice Shop**, an intentionally insecure app designed for cybersecurity training. The goal was to identify vulnerabilities, exploit them in a controlled environment, and provide professional mitigation strategies.

## 🎯 Objectives
- Demonstrate ethical offensive security testing
- Identify critical web vulnerabilities (SQLi, XSS, etc.)
- Show exploitation methodology and remediation steps
- Document findings following a professional reporting format

## 🧰 Tools Used
| Tool | Purpose |
|------|---------|
| **OWASP ZAP** | Active/Passive scanning, fuzzing |
| **Browser DevTools** | Manual testing, API inspection |
| **Docker / Local Instance** | Safe testing environment |

## 🧪 Tested Vulnerabilities (Examples)
| Vulnerability | Severity | Technique Used |
|--------------|----------|----------------|
| SQL Injection Login Bypass | 🔴 High | `' OR 1=1--` |
| Stored Cross-Site Scripting (XSS) | 🔴 High | `<svg/onload=alert()>` |
| Sensitive Data Exposure | 🟠 Medium | API enumeration |
| Missing Security Headers | 🟢 Low | Passive scan (ZAP) |

Full vulnerability details and remediation guidance are included in `Report.txt`.

## 📄 Report
🔗 **Full Professional Report:** `Report.txt` (included in repository)

## 🧑‍💻 Ethical Notice
This project was conducted in a controlled environment using **legal and intentional vulnerable targets only**. No unauthorized security testing was performed. This repository is for educational and portfolio purposes.

---

### ⭐ If you like this project, consider giving it a star and exploring more of my cybersecurity work!

