# CST8919 Lab 2 – Flask Security Demo with Azure Monitor Alerts

## Lab Overview

This lab demonstrates how to detect suspicious login activity by combining a Python Flask web application, Azure App Service, Log Analytics, and Azure Monitor alerts. It simulates a real-world scenario where failed login attempts need to be detected and acted upon promptly.

---

## Included Files

| File             | Description                                        |
|------------------|----------------------------------------------------|
| `app.py`         | Flask app with login endpoint and logging          |
| `requirements.txt` | Python dependencies (`flask`, `gunicorn`)   |
| `test-app.http`  | HTTP test requests using VS Code REST Client       |
| `.gitignore`     | Ignores virtual environment and cache files        |
| `README.md`      |                            |

---

## What I Learned

- How to deploy a Python Flask app to Azure App Service.
- How to configure logging and ensure that logs are ingested into Azure Monitor.
- How to write and test KQL (Kusto Query Language) queries to filter and analyze logs.
- How to configure alert rules that automatically notify via email when a threshold is met.

---

## Challenges Faced

- Getting logs to appear correctly in Log Analytics required enabling diagnostic settings on the App Service.
- Initially, no results were returned from the KQL query due to timing issues—solved by adjusting `TimeGenerated > ago(10m)`.
- Ensuring alerts didn’t trigger too frequently (1-minute intervals) required tuning frequency and thresholds.

---

## Real-World Improvements

- Implement IP-based throttling to avoid alert fatigue.
- Integrate with Microsoft Sentinel or Logic Apps for advanced remediation workflows.
- Use a custom detection logic based on login attempt trends per user or IP address.

---

## KQL Query with Explanation

```kql
AppServiceConsoleLogs
| where TimeGenerated > ago(10m)
| where ResultDescription has "SECURITY-ALERT"
| project TimeGenerated, ResultDescription
| order by TimeGenerated desc
```

### Explanation:
- **AppServiceConsoleLogs:** The table storing logs from our Flask app.
- **TimeGenerated > ago(10m):** Filters logs to the last 10 minutes.
- **ResultDescription has "SECURITY-ALERT":** Filters logs for failed login attempts marked as security alerts in app.py.
- **project:** Only selects relevant columns.
- **order by:** Sorts results for latest logs first.

---

## Testing
Use `test-app.http` in VS Code with the REST Client extension to test login success and failure.

---

## YouTube Video Demo
[https://youtu.be/hcLbkYLe7WE](https://youtu.be/hcLbkYLe7WE)
