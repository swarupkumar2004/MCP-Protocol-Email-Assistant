import asyncio
from email.message import EmailMessage
import aiosmtplib

EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

async def test_send():
    msg = EmailMessage()
    msg["From"] = EMAIL
    msg["To"] = EMAIL 
    msg["Subject"] = "Test Email"
    msg.set_content("This is a test email")

    try:
        result = await aiosmtplib.send(
            message=msg,
            hostname=SMTP_SERVER,
            port=SMTP_PORT,
            start_tls=True,
            username=EMAIL,
            password=PASSWORD,
        )
        print("Email sent:", result)
    except Exception as e:
        print("Error:", e)

asyncio.run(test_send())
