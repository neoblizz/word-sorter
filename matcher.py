import pandas as pd
import json
from collections import defaultdict
from difflib import SequenceMatcher
import csv

# Open the output CSV file with the characters
with open('output_file.csv', 'r', encoding='utf-8') as output_file:
    # Create a CSV reader object
    reader = csv.reader(output_file)

    # Create a default dictionary to store the best matches
    best_matches = defaultdict(list)

    # Read the input Excel file with the words to search
    input_file = pd.read_excel('input_file_to_search.xlsx')

    # Loop through each row in the output file
    for row in reader:
        # Join the characters in the row back into a word
        word = ''.join(row)

        # Loop through each row in the input file
        for _, input_row in input_file.iterrows():
            # Get the word from the input row
            input_word = input_row['word']

            # Check if all the initial characters are in the word
            if all(char in input_word for char in row):
                # Add the word and its additional columns to the best matches dictionary
                best_matches[word].append({'word': input_word, 'frequency': input_row['frequency'], 'part_of_speech': input_row['part_of_speech']})

    # Reset the input file to a pandas DataFrame to reset the file pointer
    input_file = pd.read_excel('input_file_to_search.xlsx')

# Convert the default dictionary to a regular dictionary for better JSON serialization
best_matches = dict(best_matches)

# Save the best matches dictionary to a JSON file with proper hierarchy
with open('best_matches.json', 'w', encoding='utf-8') as json_file:
    json.dump(best_matches, json_file, ensure_ascii=False, indent=4)
