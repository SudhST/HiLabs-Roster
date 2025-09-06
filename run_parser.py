import os
from parser.email_parser import parse_eml_to_json,save_parsed_email
from parser.field_extractor import extract_fields
from llm_extractor import extract_fields_with_llm
from parser.normalizer import normalize_number, normalize_date, normalize_name
from parser.excel_writer import write_to_excel
import config

def main():
    all_data = []
    for filename in os.listdir(config.EMAIL_FOLDER):
        if filename.endswith(".eml"):
            file_path = os.path.join(config.EMAIL_FOLDER, filename)
            print(f"Processing: {filename}")
            parsed_email = parse_eml_to_json(file_path)
            save_parsed_email(file_path, parsed_email)
            
            # all_data.append(fields)
            # Convert .eml → email JSON (basic structure)
            email_obj = {
                "from": parsed_email.get("from",""),  # you can expand email_parser to capture these
                "to": parsed_email.get("to",""),
                "date": parsed_email.get("date",""),
                "subject": parsed_email.get("subject",""),
                "body": parsed_email.get("body",""),  
                "table": parsed_email.get("table",""),
                "filename": filename
            }

            # Extract fields using LLM
            fields = extract_fields_with_llm(email_obj)
            
            print(f"Extracted Fields: {fields}")

            # # Normalize
            # fields["NPI"] = normalize_number(fields["NPI"])
            # fields["TIN"] = normalize_number(fields["TIN"])
            # fields["PPG"] = normalize_number(fields["PPG"])
            # fields["Effective Date"] = normalize_date(fields["Effective Date"])
            # fields["Termination Date"] = normalize_date(fields["Termination Date"])
            # fields["Provider Name"] = normalize_name(fields["Provider Name"])
            # fields["Organization Name"] = normalize_name(fields["Organization Name"])

            # all_data.append(fields)
    
    # # Write Excel
    # output_file = os.path.join(config.OUTPUT_FOLDER, "Roster_Output.xlsx")
    # write_to_excel(all_data, output_file)
    # print(f"Excel generated at: {output_file}")

if __name__ == "__main__":
    main()
