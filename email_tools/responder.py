def generate_reply(subject, sender, category="Normal"):
    if "otp" in subject.lower() or "security" in subject.lower():
        return f"Hello,\n\nWe have received your security message. No action is needed at your end.\n\nRegards,\nEmail Assistant"

    if category == "High Priority":
        return f"Hi,\n\nThank you for your urgent message. We'll get back to you shortly.\n\nRegards,\nEmail Assistant"
    elif category == "Low Priority":
        return f"Hi,\n\nThanks for reaching out. We’ve received your email.\n\nRegards,\nEmail Assistant"
    else:
        return f"Hi,\n\nThanks for your message. We’ll review it soon.\n\nRegards,\nEmail Assistant"
