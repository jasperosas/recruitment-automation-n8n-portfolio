# Set up a safe n8n demonstration

These instructions are for **synthetic applications** and an inbox controlled by the tester. The imported workflows are inactive by default.

## Option A: No-service demo (recommended first)

1. Start your own local n8n instance.
2. Import [`workflows/recruitment-routing-manual-demo.json`](workflows/recruitment-routing-manual-demo.json) from the editor's **Import from File** menu.
3. Save and click **Execute workflow**. The default fictional candidate uses `3-5 Years`.
4. In **Test Applicant (Edit Fields)**, change `Years of experience` to `6+ Years` or `0-2 Years`, then execute again.
5. Verify only the matching final Edit Fields node receives the item. This demo makes **no external requests** and sends **no email**.

## Option B: Controlled Google Sheets-to-Gmail demo

1. Create a **new Google Sheet dedicated to testing**; do not link it to a live Form. Import the eight-column header and three fictional rows from [`examples/demo-applications.csv`](examples/demo-applications.csv). Name its worksheet `Form Responses 1`.
2. Import [`workflows/recruitment-sheets-gmail-safe-demo.json`](workflows/recruitment-sheets-gmail-safe-demo.json) in a **separate** n8n workflow.
3. In **Read TEST Applications (Google Sheets)**, replace `REPLACE_WITH_TEST_SHEET_ID` with **your new test spreadsheet ID**; check the sheet tab. Configure your own Google Sheets OAuth2 credential locally, using Google Cloud's guidance for local callbacks.
4. Leave **all three Gmail nodes disabled**. Execute the workflow manually. Verify **3 items** are read and the Safety Gate lets through **exactly one** Demo Candidate A/B/C per branch.
5. If deliberately testing Gmail delivery, configure a **separate Gmail OAuth2 credential**. In **each Gmail node**, replace the non-deliverable `YOUR_TEST_INBOX@example.com` with **an inbox you control**, and personally verify the To field before executing.
6. Enable **one** Gmail node, execute **once**, verify delivery, then **disable that node**. Repeat individually for the remaining two branches only if appropriate. Do not activate the overall workflow.
7. Afterward, leave **all Gmail nodes disabled**, save the workflow and inspect its execution history for unintended sends.

**Safety details:** The Code node checks the exact fictional names, example.com email fields, job titles and experience bands; it rejects records that differ. This is a demo guardrail, not a substitute for production security controls. If the spreadsheet contains additional real records, do **not** connect or run it. Keep real applicant data isolated.

The integrated JSON has **no saved credentials**, and its Google Sheets ID and all Gmail recipients are **placeholders**. It cannot read a sheet without your configuration, and Gmail remains disabled until explicitly enabled.
