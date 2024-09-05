import csv
import json

# Define file paths
tsv_file_path = 'tel_Telu.tsv'  # Replace with your TSV file path
json_file_path = 'sentences.json'  # Path to save the JSON file

# Function to read TSV file and extract top 500 entries
def extract_top_entries(tsv_file, num_entries=500):
    entries = []
    with open(tsv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter='\t')
        
        # Read top entries
        for i, row in enumerate(reader):
            if i >= num_entries:
                break
            entries.append({
                'src_sent': row['src_sent'],
                'tgt_sent': row['tgt_sent']
            })
    
    return entries

# Function to write data to JSON file
def write_to_json(data, json_file):
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# Main script
def main():
    # Extract top 500 entries
    top_entries = extract_top_entries(tsv_file_path, num_entries=500)
    
    # Write to JSON file
    write_to_json(top_entries, json_file_path)
    
    print(f"Top 500 entries have been written to {json_file_path}")

# Run the main script
if __name__ == '__main__':
    main()
