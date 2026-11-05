# Portfolio-ready summary

## Project title

**Recruitment Application Automation — n8n, Google Sheets & Gmail**

## Description

Built a recruitment automation **prototype** in self-hosted n8n Community Edition using Docker Desktop, Google Sheets, and Gmail. The demonstration read three fictional applicants from a dedicated Google Sheet, used a Switch node to route each by experience category, and generated controlled demonstration emails to an inbox I own. I manually tested the three branches, verified all three test messages arrived, and disabled the Gmail nodes afterward. The project illustrates workflow design, OAuth integration, conditional logic and safety-conscious testing—not a deployed hiring system.

## Resume bullet

Built and locally tested an n8n automation prototype integrating Google Sheets, conditional routing and Gmail; validated three synthetic applicant paths and controlled demonstration emails using manual execution and disabled-by-default send nodes.

## Skills

n8n · Docker Desktop · Google Sheets · Gmail OAuth2 · Data mapping · Conditional branching · Testing and troubleshooting · Workflow documentation · Automation safeguards

## Demonstration evidence

- Real execution screenshot in [`assets/`](assets/recruitment-integration-test.png), displaying all three experience branches and disabled Gmail nodes.
- Owner-reported integration checks in [`TESTING.md`](TESTING.md).
- Reusable sanitized workflows in [`workflows/`](workflows/) with no active triggers, tokens, real sheet IDs or deliverable inbox addresses.

**Use accurate wording:** "Locally tested prototype" — not "production deployed" or "automated candidate screening system." The downloadable sanitized exports have not been re-executed after substitution of account-specific values.
