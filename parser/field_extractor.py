import re

def extract_fields(text):
    """
    Extract provider fields from email text.
    Returns a dictionary with required fields.
    Missing fields are marked as 'Information not found'.
    """

    fields = {
        "Transaction Type": "Information not found",
        "Transaction Attribute": "Information not found",
        "Effective Date": "Information not found",
        "Term Date": "Information not found",
        "Term Reason": "Information not found",
        "Provider Name": "Information not found",
        "Provider NPI": "Information not found",
        "Provider Specialty": "Information not found",
        "State License": "Information not found",
        "Organization Name": "Information not found",
        "TIN": "Information not found",
        "Group NPI": "Information not found",
        "Complete Address": "Information not found",
        "Phone Number": "Information not found",
        "Fax Number": "Information not found",
        "PPG ID": "Information not found",
        "Lines of Business(Medicare/Commercial/Medical)": "Information not found"
    }

    # Transaction Type
    txn_match = re.search(r"(Add|Update|Term(?:inate)?)", text, re.IGNORECASE)
    if txn_match:
        fields["Transaction Type"] = txn_match.group(1).title()

    # Transaction Attribute
    txn_attr_match = re.search(r"Transaction Attribute[:\s]+([A-Za-z\s,]+)", text, re.IGNORECASE)
    if txn_attr_match:
        fields["Transaction Attribute"] = txn_attr_match.group(1).strip()

    # Effective Date
    eff_match = re.search(r"Effective Date[:\s]+([0-9/\-]+)", text, re.IGNORECASE)
    if eff_match:
        fields["Effective Date"] = eff_match.group(1)

    # Term Date
    term_date_match = re.search(r"Term Date[:\s]+([0-9/\-]+)", text, re.IGNORECASE)
    if term_date_match:
        fields["Term Date"] = term_date_match.group(1)

    # Term Reason
    term_reason_match = re.search(r"Term Reason[:\s]+(.+)", text, re.IGNORECASE)
    if term_reason_match:
        fields["Term Reason"] = term_reason_match.group(1).strip()

    # Provider Name
    name_match = re.search(r"Provider Name[:\s]+([A-Za-z\s,.-]+)", text, re.IGNORECASE)
    if name_match:
        fields["Provider Name"] = name_match.group(1).strip()

    # Provider NPI
    npi_match = re.search(r"\b\d{10}\b", text)
    if npi_match:
        fields["Provider NPI"] = npi_match.group()

    # Provider Specialty
    spec_match = re.search(r"Provider Specialty[:\s]+([A-Za-z\s/]+)", text, re.IGNORECASE)
    if spec_match:
        fields["Provider Specialty"] = spec_match.group(1).strip()

    # State License
    lic_match = re.search(r"State License[:\s]+([A-Za-z0-9-]+)", text, re.IGNORECASE)
    if lic_match:
        fields["State License"] = lic_match.group(1)

    # Organization Name
    org_match = re.search(r"Organization Name[:\s]+([A-Za-z\s,.-]+)", text, re.IGNORECASE)
    if org_match:
        fields["Organization Name"] = org_match.group(1).strip()

    # TIN
    tin_match = re.search(r"\b\d{9}\b", text)
    if tin_match:
        fields["TIN"] = tin_match.group()

    # Group NPI
    group_npi_match = re.search(r"Group NPI[:\s]+([A-Za-z0-9-]+)", text, re.IGNORECASE)
    if group_npi_match:
        fields["Group NPI"] = group_npi_match.group(1)

    # Complete Address
    addr_match = re.search(r"Complete Address[:\s]+(.+)", text, re.IGNORECASE)
    if addr_match:
        fields["Complete Address"] = addr_match.group(1).strip()

    # Phone Number
    phone_match = re.search(r"Phone Number[:\s]+([\d\-\(\)\s]+)", text, re.IGNORECASE)
    if phone_match:
        fields["Phone Number"] = phone_match.group(1)

    # Fax Number
    fax_match = re.search(r"Fax Number[:\s]+([\d\-\(\)\s]+)", text, re.IGNORECASE)
    if fax_match:
        fields["Fax Number"] = fax_match.group(1)

    # PPG ID
    ppg_match = re.findall(r"PPG ID[:\s]+([A-Za-z0-9-]+)", text, re.IGNORECASE)
    if ppg_match:
        fields["PPG ID"] = ", ".join(ppg_match)

    # Lines of Business
    lob_match = re.search(r"Lines of Business[:\s]+([A-Za-z\s,]+)", text, re.IGNORECASE)
    if lob_match:
        fields["Lines of Business(Medicare/Commercial/Medical)"] = lob_match.group(1).replace(";", ",").strip()

    return fields
