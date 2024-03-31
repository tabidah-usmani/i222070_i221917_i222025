#!/usr/bin/env python3

import sys
import csv
import re

# tokenizes text
def tokenize_text(text):
     #tokenize text by finding words
    tokens = re.findall(r'\b[A-Za-z]+\b', text.lower())
    return tokens

def mapper():
    csv_reader = csv.reader(sys.stdin)
    word_id_mapping = {}  # dictionary to map words to unique IDs
    current_id = 0  #  # initialize current ID counter

    #iterate over each row in the CSV input
    for row in csv_reader:
        if len(row) == 2:   #row has two elements
            section_text = row[1]
             #tokenize the text of the article
            tokens = tokenize_text(section_text)
            for token in tokens:
                if token not in word_id_mapping:
                    # assign a unique ID to each word
                    word_id_mapping[token] = current_id
                    current_id += 1
                     # output word ID and article ID with frequency
                print(f"{word_id_mapping[token]}\t{row[0]}:1")  #emit word ID and article ID with frequency

if __name__ == "__main__":
    mapper()

