import csv

# Open the CSV file
with open('input_words.csv', 'r', encoding='utf-8') as input_file:
    # Create a CSV reader object
    reader = csv.reader(input_file)

    # Open a new CSV file to write the output
    with open('output_file.csv', 'w', encoding='utf-8', newline='') as output_file:
        # Create a CSV writer object
        writer = csv.writer(output_file)

        # Loop through each row in the input file
        for row in reader:
            # Get the word from the first column
            word = row[0]

            # Split the word into individual characters
            characters = list(word)

            # Write the characters to new columns in the output file
            writer.writerow(characters)