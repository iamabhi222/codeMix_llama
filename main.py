import csv
import json

# Define file paths
tsv_file_path = 'hin_Deva.tsv'  # Replace with your TSV file path
json_file_path = 'hin_sentences.json'  # Path to save the JSON file

# Function to count the number of words in a sentence
def count_words(sentence):
    if isinstance(sentence, str):
        return len(sentence.split())
    return 0

# Function to read TSV file and extract top entries with sentence length check
def extract_top_entries(tsv_file, num_entries=500, max_words=50):
    entries = []
    with open(tsv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter='\t')
        
        # Read top entries with length check
        for row in reader:
            src_sent = row.get('src_sent', '')
            tgt_sent = row.get('tgt_sent', '')
            src_len = count_words(src_sent)
            tgt_len = count_words(tgt_sent)
            
            # Check if both sentences are within the maximum word limit
            if src_len <= max_words and tgt_len <= max_words:
                entries.append({
                    'src_sent': src_sent,
                    'tgt_sent': tgt_sent
                })
            
            # Stop if the desired number of valid entries is reached
            if len(entries) >= num_entries:
                break
    
    return entries

# Function to write data to JSON file
def write_to_json(data, json_file):
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# Main script
def main():
    # Extract top 500 entries with sentence length check
    top_entries = extract_top_entries(tsv_file_path, num_entries=500, max_words=50)
    
    # Write to JSON file
    write_to_json(top_entries, json_file_path)
    
    print(f"Top {len(top_entries)} entries with sentences not exceeding 20 words have been written to {json_file_path}")

# Run the main script
if __name__ == '__main__':
    main()
