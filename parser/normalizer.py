import re
from datetime import datetime

def normalize_number(value):
    if value == "Information not found":
        return value
    return re.sub(r'\D', '', value)

def normalize_date(value):
    if value == "Information not found":
        return value
    try:
        dt = datetime.strptime(value, "%m/%d/%Y")
    except:
        # try other formats
        try:
            dt = datetime.strptime(value, "%Y-%m-%d")
        except:
            return "Information not found"
    return dt.strftime("%m/%d/%Y")

def normalize_name(value):
    if value == "Information not found":
        return value
    return " ".join(value.strip().title().split())
