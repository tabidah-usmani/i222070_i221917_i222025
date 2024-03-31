#!/usr/bin/env python3

import sys
import csv
import re

# tokenizes text
def tokenize_text(text):
    tokens = re.findall(r'\b[A-Za-z]+\b', text.lower())
    return tokens

def mapper():
    csv_reader = csv.reader(sys.stdin)
    word_id_mapping = {}  # map word to unique ID
    current_id = 0  # current ID counter
    
    for row in csv_reader:
        if len(row) == 2:
            section_text = row[1]
            tokens = tokenize_text(section_text)
            for token in tokens:
                if token not in word_id_mapping:
                    word_id_mapping[token] = current_id
                    current_id += 1
                print(f"{word_id_mapping[token]}\t{row[0]}:1")  #emit word ID and article ID with frequency

if __name__ == "__main__":
    mapper()

