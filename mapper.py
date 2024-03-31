#!/usr/bin/env python3

import sys
import csv
import re

def tokenize_text(text):
    # Tokenize the text using regular expression
    tokens = re.findall(r'\b[A-Za-z]+\b', text.lower())
    return tokens

def mapper():
    # Read input from standard input (stdin)
    csv_reader = csv.reader(sys.stdin)

    # Initialize a dictionary to store term frequencies for each article ID
    article_term_frequencies = {}

    # Iterate over each row in the CSV file
    for row in csv_reader:
        if len(row) == 2:  # Ensure there are two columns
            article_id, section_text = row
            # Tokenize the section text
            tokens = tokenize_text(section_text)
            # Initialize a dictionary to store term frequencies for the current article ID
            term_frequencies = {}
            # Count the frequency of each term in the current article ID
            for term in tokens:
                # If the term exists in the token_id_mapping, assign its ID
                if term in token_id_mapping:
                    term_id = token_id_mapping[term]
                    term_frequencies[term_id] = term_frequencies.get(term_id, 0) + 1
            # Store term frequencies for the current article ID in the article_term_frequencies dictionary
            article_term_frequencies[article_id] = term_frequencies

    # Output term frequencies for each article ID
    for article_id, term_frequencies in article_term_frequencies.items():
        for term_id, frequency in term_frequencies.items():
            print(f"({term_id}, {article_id}, {frequency})")

if __name__ == "__main__":
    mapper()
