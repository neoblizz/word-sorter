import json
import pandas as pd

# Load the output file containing the characters of interest
output_file = pd.read_csv('input_words.csv', encoding='utf-8')

# Load the input file containing all words to search
input_file = pd.read_excel('input_file_to_search.xlsx')

# Create an empty dictionary to hold the results
results = {}

# Iterate over each row in the output file
for _, row in output_file.iterrows():

    # Extract the characters of interest
    characters = list(row[0])

    # Create a list to hold the matching words
    matching_words = []

    # Iterate over each row in the input file
    for _, word_row in input_file.iterrows():

        # Extract the word to check
        word = word_row['word']

        # Check if all characters are in the word
        if all(char in word for char in characters):
            
            # Add the word to the list of matching words
            matching_words.append({
                'word': word,
                'frequency': word_row['frequency'],
                'part_of_speech': word_row['part_of_speech']
            })

    # Add the matching words to the results dictionary
    results[''.join(characters)] = matching_words

# Save the results as a JSON file
with open('results.json', 'w', encoding='utf-8') as outfile:
    json.dump(results, outfile, ensure_ascii=False, indent=4)