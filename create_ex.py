import json
import pandas as pd

# Load JSON data
with open('sentences.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Initialize a list to hold all data
records = []

# Process the JSON data
for batch_name, sentences in data.items():
    for item in sentences:
        records.append({
            'src_sent': item.get('src_sent', ''),
            'tgt_sent': item.get('tgt_sent', ''),
            'codeMix': item.get('codeMix', '')  # Ensure the 'codeMix' field is included
        })

# Create a DataFrame from the records
df = pd.DataFrame(records)

# Save DataFrame to an Excel file
excel_file_path = 'sentences.xlsx'
df.to_excel(excel_file_path, index=False)

print(f"Excel file has been created: {excel_file_path}")
