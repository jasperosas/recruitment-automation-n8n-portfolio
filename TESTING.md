# Test record and evidence

**Test date:** 5 November 2026  
**Environment:** Windows laptop, Docker Desktop, self-hosted n8n Community Edition  
**Data:** Fictional test records only  
**Source:** Project owner's real-world test reports and supplied screenshot  
**Publication:** This is a sanitized *public copy* created later; its exported files were not re-executed after redaction.

| Check | Scope | Evidence / outcome |
| --- | --- | --- |
| Manual routing | Six-node manual workflow without external integrations | Owner reported correct paths for `6+ Years`, `3-5 Years`, `0-2 Years` |
| Google Sheets integration | Dedicated fictional-data sheet; read-only node | Owner reported successful execution, three rows; screenshot shows 3 items leaving Sheets read node |
| Gmail standalone | One manually initiated email to owner's inbox | Owner reported receipt |
| Integrated Gmail: 6+ | Manually enabled one Gmail branch | Owner reported receipt |
| Integrated Gmail: 3-5 | Manually enabled one Gmail branch | Owner reported receipt |
| Integrated Gmail: 0-2 | Manually enabled one Gmail branch | Owner reported receipt |
| Post-test | Three Gmail nodes disabled; no active trigger | Screenshot shows all 3 Gmail nodes deactivated; owner confirmed disabled |

## Screenshot of actual local execution

![Local n8n test execution showing three fictional candidates routed, and deactivated Gmail nodes](assets/recruitment-integration-test.png)

The screenshot visibly includes a manual trigger, a Google Sheets read, a fictional-record safety gate, three experience outputs, and deactivated Gmail nodes. There is **one item per experience branch**. It supports **execution and routing** observations, **not independent receipt of delivered emails**.

## Architecture: original archive vs. safe test

The original archived n8n workflow had a Google Sheets `rowAdded` trigger, applicant acknowledgment, HR notification and routing to invitation or keep-on-file messaging. That **original archival workflow was not re-tested end to end**. The local successful tests were conducted in **separate manual demo workflows**, intentionally avoiding live forms and real recipients.

## Not tested or not verified

- Automatic triggering after a real Google Form submission or on live Sheets row addition.
- Applicant acknowledgment and HR notification nodes from the original archived workflow.
- Emailing real candidates or processing real applications.
- OAuth-expiry recovery, duplicate-row/duplicate-send behavior, rate limits, outages, simultaneous executions or malicious input.
- Hiring outcome suitability, bias/fairness, legal compliance, or production readiness.

**Note:** This demonstration uses experience bands solely to show routing logic. Actual hiring processes require human review and appropriate hiring/privacy policies.
