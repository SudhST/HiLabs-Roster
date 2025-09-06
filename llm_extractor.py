import requests
import json

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "llama3.2:3b"

def extract_fields_with_llm(email_obj):    

    # Combine useful parts of the email into a single text
    email_text = f"""
    From: {email_obj.get('from', '')}
    To: {email_obj.get('to', '')}
    date: {email_obj.get('date', '')}
    Subject: {email_obj.get('subject', '')}
    Body:{email_obj.get('body', '')}
    Table:{email_obj.get('tables', '')}
    Filename: {email_obj.get('filename', '')}
    """

    # Define JSON schema for structured output
    schema = {
        "type": "object",
        "properties": {
            "Transaction Type": {"type": "string"},
            "Provider Name": {"type": "string"},
            "NPI": {"type": "string"},
            "TIN": {"type": "string"},
            "State License": {"type": "string"},
            "Specialty": {"type": "string"},
            "Subspecialty": {"type": "string"},
            "Effective Date": {"type": "string"},
            "Termination Date": {"type": "string"},
            "Lines of Business": {"type": "string"},
            "PPG": {"type": "string"},
            "Organization Name": {"type": "string"},
            "Address": {"type": "string"},
            "City": {"type": "string"},
            "State": {"type": "string"},
            "ZIP": {"type": "string"},
            "Phone": {"type": "string"},
            "Fax": {"type": "string"},
            "Email": {"type": "string"},
        },
        "required": [
            "Transaction Type","Provider Name","NPI","TIN","State License","Specialty",
            "Subspecialty","Effective Date","Termination Date","Lines of Business",
            "PPG","Organization Name","Address","City","State","ZIP","Phone","Fax","Email"
        ]
    }
    with open("system_prompt.txt", "r") as f:
        system_prompt = f.read()      
    
    payload = {
        "model": MODEL_NAME,
        "stream": False,  # structured output needs non-streaming mode
        "messages": [
            {
                "role": "system",
                "content": (
                    system_prompt
                )
            },
            {
                "role": "user",
                "content": f"Extract provider information from this email:\n\n{email_text}"
            }
        ],
        "format": schema
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code != 200:
        raise RuntimeError(f"Ollama API error {response.status_code}: {response.text}")

    result = response.json()

    # Structured output is directly in `message.content`
    try:
        extracted = json.loads(result["message"]["content"])
    except (KeyError, json.JSONDecodeError):
        raise ValueError("Failed to parse structured JSON response from model.")

    return extracted
