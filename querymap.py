#!/usr/bin/env python3

import sys
import re

def tokenize_text(text):
    tokens = re.findall(r'\b[A-Za-z]+\b', text.lower())
    return tokens

def query_mapper():
    query = sys.stdin.readline().strip()  # read query from input
    tokens = tokenize_text(query)  # tokenize query
    
    for token in tokens:
        print(f"{token}\t1")  # emit token with frequency 1

if __name__ == "__main__":
    query_mapper()
