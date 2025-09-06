import os
from parser.email_parser import extract_email_body
from parser.field_extractor import extract_fields
from parser.normalizer import normalize_number, normalize_date, normalize_name
from parser.excel_writer import write_to_excel
import config

def main():
    all_data = []
    
    for filename in os.listdir(config.EMAIL_FOLDER):
        if filename.endswith(".eml"):
            file_path = os.path.join(config.EMAIL_FOLDER, filename)
            print(f"Processing: {filename}")
            
            body = extract_email_body(file_path)
            fields = extract_fields(body)
            
            # Normalize data
            fields["NPI"] = normalize_number(fields["NPI"])
            fields["TIN"] = normalize_number(fields["TIN"])
            fields["PPG"] = normalize_number(fields["PPG"])
            fields["Effective Date"] = normalize_date(fields["Effective Date"])
            fields["Provider Name"] = normalize_name(fields["Provider Name"])
            
            all_data.append(fields)
    
    # Write Excel
    output_file = os.path.join(config.OUTPUT_FOLDER, "Roster_Output.xlsx")
    write_to_excel(all_data, output_file)
    print(f"Excel generated at: {output_file}")

if __name__ == "__main__":
    main()
