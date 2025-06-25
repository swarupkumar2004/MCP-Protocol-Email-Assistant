def categorize_email(subject, sender):
    subject = subject.lower()
    sender = sender.lower()

    if any(keyword in subject for keyword in ["otp", "security", "alert", "urgent", "action required"]):
        return "High Priority"
    elif any(keyword in subject for keyword in ["newsletter", "offer", "sale", "promotion", "discount"]):
        return "Low Priority"
    elif "no-reply" in sender or "notification" in sender:
        return "Medium Priority"
    else:
        return "Normal"
