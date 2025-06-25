import imaplib
import email
import base64
import asyncio
from email.header import decode_header
from email_tools.categorizer import categorize_email
from oauth_login import get_gmail_credentials  # ✅ keep this!

IMAP_SERVER = "imap.gmail.com"
IMAP_PORT = 993

def generate_oauth2_string(email, access_token):
    return f"user={email}\1auth=Bearer {access_token}\1\1"

async def read_emails(context=None):
    try:
        creds = get_gmail_credentials()
        access_token = creds.token
        email_address = creds._id_token.get("email")

        mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
        auth_string = generate_oauth2_string(email_address, access_token)
        mail.authenticate("XOAUTH2", lambda x: auth_string.encode())

        mail.select("inbox")
        status, messages = mail.search(None, "ALL")
        email_ids = messages[0].split()
        latest_email_ids = email_ids[-5:]

        emails = []

        for eid in reversed(latest_email_ids):
            status, msg_data = mail.fetch(eid, "(RFC822)")
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)

            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding or "utf-8")

            from_ = msg.get("From")
            category = categorize_email(subject, from_)
            emails.append({"from": from_, "subject": subject, "category": category})

        mail.logout()
        return {"status": "success", "emails": emails}

    except Exception as e:
        return {"status": "error", "message": str(e)}
