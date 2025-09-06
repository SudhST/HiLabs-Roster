import email
from email import policy
from bs4 import BeautifulSoup
import pandas as pd
import json
import os


def parse_eml_to_json(eml_file):
    # Read raw email file
    with open(eml_file, 'r', encoding='utf-8') as f:
        msg = email.message_from_file(f, policy=policy.default)

    # Extract headers
    email_dict = {
        "subject": msg.get("subject"),
        "from": msg.get("from"),
        "to": msg.get("to"),
        "date": msg.get("date"),
        "body": None,
        "tables": []
    }

    # Get email body (plain or HTML)
    body = None
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == "text/plain":
                body = part.get_content()
            elif content_type == "text/html":
                body = part.get_content()
    else:
        body = msg.get_content()

    # Clean body: extract only visible text, remove tables
    clean_body = None
    if body:
        soup = BeautifulSoup(body, "html.parser")
        # Remove script/style/table tags
        for tag in soup(["script", "style", "table"]):
            tag.decompose()
        clean_body = soup.get_text(separator="\n", strip=True)

    email_dict["body"] = clean_body if clean_body else None

    # Parse HTML tables into JSON arrays
    if body:
        soup = BeautifulSoup(body, "html.parser")
        tables = soup.find_all("table")

        for table in tables:
            df = pd.read_html(str(table))[0]  # Convert table to DataFrame
            table_json = df.to_dict(orient="records")
            email_dict["tables"].append(table_json)

    return email_dict


def save_parsed_email(eml_file, parsed_email):
    # Ensure output directory exists
    os.makedirs("parsed_emails", exist_ok=True)

    # Build output file path (same name as input, but .txt)
    base_name = os.path.splitext(os.path.basename(eml_file))[0]
    out_file = os.path.join("parsed_emails", f"{base_name}.txt")

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(json.dumps(parsed_email, indent=4, ensure_ascii=False))

    print(f"Parsed email saved to {out_file}")


if __name__ == "__main__":
    eml_file = "sample.eml"
    parsed_email = parse_eml_to_json(eml_file)
    save_parsed_email(eml_file, parsed_email)