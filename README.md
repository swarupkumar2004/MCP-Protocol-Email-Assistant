# MCP-Protocol-Email-Assistant

# ✉️ MCP Email Assistant

This is a Python-based Gmail Email Assistant capable of:
- 🔍 Reading recent emails from your Gmail inbox
- 🕒 Scheduling a reply after a custom delay
- 🧠 Categorizing incoming emails using basic logic

It uses Google's OAuth 2.0 and Gmail API to function.

---

## 🚀 Features

- OAuth2.0 Authentication with Gmail
- Read and categorize recent inbox emails
- Schedule delayed email replies
- Fully modular architecture (scheduler, categorizer, oauth, server)

---

## 🧰 Requirements

- Python 3.8+
- pip
- Gmail account

---

## 📦 Installation

1. Clone the repo or download the files:

```bash
git clone https://github.com/yourname/mcp-email-assistant.git
cd mcp-email-assistant
````

2. Create and activate a virtual environment:

```bash
python -m venv mvenv
mvenv\Scripts\activate  # For Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔐 Gmail API Setup (OAuth2.0)

You must configure OAuth before using the app.

### Step 1: Create OAuth Client

* Go to [Google Cloud Console](https://console.cloud.google.com/)
* Create a new project
* Enable Gmail API (APIs & Services → Library → Gmail API → Enable)
* Go to “OAuth consent screen”

  * Set user type to External
  * Fill in App name and email
  * Add your Gmail in Test Users tab
* Go to “Credentials”

  * Create Credentials → OAuth Client ID → Application type: Desktop App
  * Download the credentials JSON

### Step 2: Add Required Files

Place the downloaded JSON file as:

```
credentials.json  ← Required for Gmail authentication
token.pickle      ← Will be auto-generated after login
```

❗️❗️ Note: These files are sensitive and were NOT uploaded for security reasons.

---

## 🧪 First-Time Authentication

Run this command to authenticate and generate the token:

```bash
python oauth_login.py
```

A browser will open asking you to log into Gmail and authorize access.

After success, token.pickle will be generated.

---

## ▶️ Running the Assistant

To launch the email assistant server:

```bash
python mcp_server.py
```

---

## 🛠 Project Structure

```
MCP_Email/
├── oauth_login.py            ← Handles Google OAuth
├── mcp_server.py             ← Main server that ties tools
├── email_tools/
│   ├── reader.py             ← Reads and categorizes emails
│   ├── scheduler.py          ← Sends delayed replies
│   ├── categorizer.py        ← Categorizes by keywords
├── credentials.json          ← 🔒 Your Gmail OAuth client file (Not uploaded)
├── token.pickle              ← 🔒 Generated token after login (Not uploaded)
└── requirements.txt
```

---

## ✉️ Example Tool Usage

✅ Email Scheduler

```python
await schedule_email_send(
    to_email="someone@example.com",
    subject="Follow up",
    body="This is a delayed email.",
    delay_seconds=10
)
```

✅ Read Emails

```python
emails = await read_emails()
print(emails)
```

---

## 📎 Notes

* Always keep `credentials.json` and `token.pickle` safe.
* You must re-authenticate if you delete the token.pickle file.
* OAuth tokens will expire after a while but auto-refresh if stored correctly.

---
