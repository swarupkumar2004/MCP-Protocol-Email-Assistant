import asyncio
import base64
from email.message import EmailMessage
import smtplib
from oauth_login import get_gmail_credentials
from googleapiclient.discovery import build

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def generate_oauth2_string(email_address, access_token):
    auth_string = f"user={email_address}\1auth=Bearer {access_token}\1\1"
    return base64.b64encode(auth_string.encode("utf-8")).decode()

def get_user_email(creds):
    if creds and getattr(creds, "_id_token", None):
        email = creds._id_token.get("email")
        if email:
            return email
    service = build('gmail', 'v1', credentials=creds)
    profile = service.users().getProfile(userId='me').execute()
    return profile.get("emailAddress")

async def schedule_email_send(to_email, subject, body, delay_seconds=10):
    await asyncio.sleep(delay_seconds)

    creds = get_gmail_credentials()
    access_token = creds.token
    email_address = get_user_email(creds)
    msg = EmailMessage()
    msg["From"] = email_address
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        xoauth2_string = generate_oauth2_string(email_address, access_token)
        server.docmd("AUTH", "XOAUTH2 " + xoauth2_string)

        server.send_message(msg)
        server.quit()

        return {
            "status": "success",
            "message": f"Email sent to {to_email} after {delay_seconds} seconds"
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}
