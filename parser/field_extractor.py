import re

def extract_fields(text):
    """
    Extract provider fields from email text.
    Returns a dictionary with required fields.
    """
    # Initialize dictionary with default "Information not found"
    fields = {
        "Provider Name": "Information not found",
        "NPI": "Information not found",
        "TIN": "Information not found",
        "State License": "Information not found",
        "Specialty": "Information not found",
        "Effective Date": "Information not found",
        "Lines of Business": "Information not found",
        "PPG": "Information not found"
    }
    
    # Example regex extraction (you can expand per email format)
    npi_match = re.search(r"\b\d{10}\b", text)
    if npi_match:
        fields["NPI"] = npi_match.group()
    
    tin_match = re.search(r"\b\d{9}\b", text)
    if tin_match:
        fields["TIN"] = tin_match.group()
    
    # Provider Name example
    name_match = re.search(r"Provider Name[:\s]+([A-Za-z\s]+)", text)
    if name_match:
        fields["Provider Name"] = name_match.group(1).strip()
    
    # Add more regex for other fields as needed
    
    return fields
