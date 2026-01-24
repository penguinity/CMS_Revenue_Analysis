import pandas as pd
from pathlib import Path
import os
import re

def norm(s):
    s = str(s)
    s = s.replace("\n", " ").replace("\r", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return s.lower()

def extract_healthcare_master_data(file_path):
    file_path = Path(file_path)

    print("CWD:", os.getcwd())
    print("Using file:", file_path.resolve())
    print("Exists?:", file_path.exists())

    if not file_path.exists():
        return f"File not found: {file_path.resolve()}"

    xl = pd.ExcelFile(file_path, engine="openpyxl")
    print("Sheets found:", xl.sheet_names)

    targets = ["United States", "North Carolina"]
    master_results = {region: {} for region in targets}

    cols_mapping = {
        'Total Original Medicare Part A Enrollees': 'Enrollees',
        'Total Discharges': 'Total_Discharges',
        'Total Discharges Beginning with Emergency Room Visit': 'ER_Discharges',
        'Discharges Per 1,000 Original Medicare Part A Enrollees': 'Discharges_per_1k_Enrollees',
        'Total Days of Care Per Discharge': 'Avg_Length_of_Stay',
        'Program Payments Per Discharge': 'Avg_Payment_per_Discharge',
        'Discharged Dead': 'Deaths'
    }

    # pre-normalize desired headers for fuzzy matching
    wanted_norm = {norm(k): k for k in cols_mapping.keys()}

    for sheet in xl.sheet_names:
        df_check = pd.read_excel(xl, sheet_name=sheet, header=None, nrows=30)
        df_check = df_check.astype(str).map(norm)

        header_row_index = None
        for idx, row in df_check.iterrows():
            row_vals = [str(v) for v in row.values if str(v) != "nan"]
            if any(any(w in cell for cell in row_vals) for w in wanted_norm.keys()):
                header_row_index = idx
                break

        if header_row_index is None:
            continue

        # Use header=header_row_index
        df = pd.read_excel(xl, sheet_name=sheet, header=header_row_index, engine="openpyxl")
        df.columns = [re.sub(r"\s+", " ", str(c).replace("\n", " ")).strip() for c in df.columns]

        # first column assumed geographic label
        geo_col = df.columns[0]
        df[geo_col] = df[geo_col].astype(str).str.strip()

        matches = df[df[geo_col].isin(targets)].copy()
        if matches.empty:
            continue

        for _, row in matches.iterrows():
            region = row[geo_col].strip()
            for raw_col, clean_name in cols_mapping.items():
                if raw_col in df.columns:
                    val = row.get(raw_col)
                    if isinstance(val, str):
                        val = val.replace('$', '').replace(',', '').strip()
                    num_val = pd.to_numeric(val, errors='coerce')
                    if pd.notnull(num_val) and clean_name not in master_results[region]:
                        master_results[region][clean_name] = num_val

    final_df = pd.DataFrame.from_dict(master_results, orient='index').reset_index().rename(columns={'index': 'Region'})

    if 'ER_Discharges' in final_df.columns and 'Total_Discharges' in final_df.columns:
        final_df['ER_Dependency_Per'] = (final_df['ER_Discharges'] / final_df['Total_Discharges']) * 100

    if 'Deaths' in final_df.columns and 'Total_Discharges' in final_df.columns:
        final_df['Mortality_Rate_Pct'] = (final_df['Deaths'] / final_df['Total_Discharges']) * 100

    return final_df


# execution
file_path = "CPS MDCR INPT 2021.xlsx"
results = extract_healthcare_master_data(file_path)

if isinstance(results, pd.DataFrame) and not results.empty:
    output_name = "NC_vs_US_Healthcare_Final_Consolidated.xlsx"
    results.to_excel(output_name, index=False)
    print("✅ Success:")
    print(results)
else:
    print("❌ No data found / error:")
    print(results)
