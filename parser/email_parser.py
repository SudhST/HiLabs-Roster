import email
from email import policy

def extract_email_body(file_path):
    """Reads a .eml file and returns its text content."""
    with open(file_path, "rb") as f:
        msg = email.message_from_binary_file(f, policy=policy.default)
    
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body += part.get_content()
    else:
        body = msg.get_content()
    return body
