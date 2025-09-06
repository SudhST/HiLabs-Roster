import re

def extract_fields(text):
    """
    Extract provider fields from email text.
    Returns a dictionary with required fields.
    Missing fields are marked as 'Information not found'.
    """

    fields = {
        "Transaction Type": "Information not found",
        "Provider Name": "Information not found",
        "NPI": "Information not found",
        "TIN": "Information not found",
        "State License": "Information not found",
        "Specialty": "Information not found",
        "Subspecialty": "Information not found",
        "Effective Date": "Information not found",
        "Termination Date": "Information not found",
        "Lines of Business": "Information not found",
        "PPG": "Information not found",
        "Organization Name": "Information not found",
        "Address": "Information not found",
        "City": "Information not found",
        "State": "Information not found",
        "ZIP": "Information not found",
        "Phone": "Information not found",
        "Fax": "Information not found",
        "Email": "Information not found"
    }

    # Transaction Type
    txn_match = re.search(r"(Add|Update|Term(?:inate)?)", text, re.IGNORECASE)
    if txn_match:
        fields["Transaction Type"] = txn_match.group(1).title()

    # Provider Name
    name_match = re.search(r"Provider Name[:\s]+([A-Za-z\s,.-]+)", text, re.IGNORECASE)
    if name_match:
        fields["Provider Name"] = name_match.group(1).strip()

    # NPI
    npi_match = re.search(r"\b\d{10}\b", text)
    if npi_match:
        fields["NPI"] = npi_match.group()

    # TIN
    tin_match = re.search(r"\b\d{9}\b", text)
    if tin_match:
        fields["TIN"] = tin_match.group()

    # State License
    lic_match = re.search(r"License[:\s]+([A-Za-z0-9-]+)", text, re.IGNORECASE)
    if lic_match:
        fields["State License"] = lic_match.group(1)

    # Specialty
    spec_match = re.search(r"Specialty[:\s]+([A-Za-z\s/]+)", text, re.IGNORECASE)
    if spec_match:
        fields["Specialty"] = spec_match.group(1).strip()

    # Subspecialty
    subspec_match = re.search(r"Subspecialty[:\s]+([A-Za-z\s/]+)", text, re.IGNORECASE)
    if subspec_match:
        fields["Subspecialty"] = subspec_match.group(1).strip()

    # Effective Date
    eff_match = re.search(r"Effective Date[:\s]+([0-9/\-]+)", text, re.IGNORECASE)
    if eff_match:
        fields["Effective Date"] = eff_match.group(1)

    # Termination Date
    term_match = re.search(r"Termination Date[:\s]+([0-9/\-]+)", text, re.IGNORECASE)
    if term_match:
        fields["Termination Date"] = term_match.group(1)

    # Lines of Business
    lob_match = re.search(r"Lines of Business[:\s]+([A-Za-z\s,]+)", text, re.IGNORECASE)
    if lob_match:
        fields["Lines of Business"] = lob_match.group(1).strip()

    # PPG
    ppg_match = re.search(r"PPG[:\s]+([A-Za-z0-9-]+)", text, re.IGNORECASE)
    if ppg_match:
        fields["PPG"] = ppg_match.group(1)

    # Organization / Group Name
    org_match = re.search(r"Organization Name[:\s]+([A-Za-z\s,.-]+)", text, re.IGNORECASE)
    if org_match:
        fields["Organization Name"] = org_match.group(1).strip()

    # Address
    addr_match = re.search(r"Address[:\s]+(.+)", text, re.IGNORECASE)
    if addr_match:
        fields["Address"] = addr_match.group(1).strip()

    # City
    city_match = re.search(r"City[:\s]+([A-Za-z\s]+)", text, re.IGNORECASE)
    if city_match:
        fields["City"] = city_match.group(1).strip()

    # State
    state_match = re.search(r"State[:\s]+([A-Z]{2})", text, re.IGNORECASE)
    if state_match:
        fields["State"] = state_match.group(1).upper()

    # ZIP
    zip_match = re.search(r"\b\d{5}(?:-\d{4})?\b", text)
    if zip_match:
        fields["ZIP"] = zip_match.group()

    # Phone
    phone_match = re.search(r"Phone[:\s]+([\d\-\(\)\s]+)", text, re.IGNORECASE)
    if phone_match:
        fields["Phone"] = phone_match.group(1)

    # Fax
    fax_match = re.search(r"Fax[:\s]+([\d\-\(\)\s]+)", text, re.IGNORECASE)
    if fax_match:
        fields["Fax"] = fax_match.group(1)

    # Email
    email_match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    if email_match:
        fields["Email"] = email_match.group()

    return fields
