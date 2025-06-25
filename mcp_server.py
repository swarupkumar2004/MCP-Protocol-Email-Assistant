import asyncio
from mcp_mock import MCPServer
from email_tools.reader import read_emails
from email_tools.responder import generate_reply
from email_tools.scheduler import schedule_email_send

server = MCPServer("email-assistant")

@server.tool("read_inbox")
async def read_inbox_tool(context):
    return await read_emails()

@server.tool("send_reply_later")
async def send_reply_tool(context):
    to_email = "your_test_email@example.com"
    subject = "Thanks for your message"
    body = "Hi,\n\nThis is a test response.\n\nRegards,\nEmail Assistant"
    return await schedule_email_send(to_email, subject, body)

if __name__ == "__main__":
    server.run()

    print("\nFetching recent emails...")
    result = asyncio.run(read_inbox_tool(None))
    for idx, email_data in enumerate(result.get("emails", []), start=1):
        print(f"{idx}. [{email_data['category']}] From: {email_data['from']}, Subject: {email_data['subject']}")
        reply = generate_reply(email_data["subject"], email_data["from"], email_data["category"])
        print(f"Draft Reply:\n{reply}\n")

    print("Scheduling reply email in 10 seconds...")
    result = asyncio.run(send_reply_tool(None))
    print("Email Scheduler:", result)
