import re

# Read the raw email content from the file
with open("email.txt", "r") as file:
    email_content = file.read()

# Regular expressions for extracting data
sender_email_pattern = r"^From:.*<(.+?)>"
recipient_email_pattern = r"^To:.*<(.+?)>"
subject_pattern = r"^Subject: (.+)"
body_pattern = r"(\n\n.+)$"  # Captures everything after the first double newline

# Extract sender email address
sender_email_match = re.search(sender_email_pattern, email_content, re.MULTILINE)
sender_email = sender_email_match.group(1) if sender_email_match else None

# Extract recipient email address
recipient_email_match = re.search(recipient_email_pattern, email_content, re.MULTILINE)
recipient_email = recipient_email_match.group(1) if recipient_email_match else None

# Extract email subject
subject_match = re.search(subject_pattern, email_content, re.MULTILINE)
subject = subject_match.group(1) if subject_match else None

# Extract email body
body_match = re.search(body_pattern, email_content, re.DOTALL)
body = body_match.group(1).strip() if body_match else None

# Print the extracted information
print("Sender Email Address:", sender_email)
print("Recipient Email Address:", recipient_email)
print("Email Subject:", subject)
print("Email Body:", body)