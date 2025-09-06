import pandas as pd
import os

def write_to_excel(data_list, output_path):
    """
    Writes a list of field dictionaries to Excel.
    """
    df = pd.DataFrame(data_list)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_excel(output_path, index=False)
