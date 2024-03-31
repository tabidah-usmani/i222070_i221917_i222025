#!/usr/bin/env python3

import sys

def reducer():
    current_word = None
    term_id_mapping = {}
    current_id = 0
    word_frequencies = {}  # Dictionary to store word frequencies per article ID

    # Process input from mapper via standard input (stdin)
    for line in sys.stdin:
        # Parse the token, article ID, and frequency from the input
        term_id, article_id, frequency = map(int, line.strip().split('\t'))

        # If the word changes or it's the first word
        if current_word != term_id:
            # Output word frequencies for the previous word
            if current_word is not None:
                for article_id, freq in word_frequencies.items():
                    print(f"({current_word}, {article_id}, {freq})")

            # Update current word
            current_word = term_id

            # Reset word frequencies
            word_frequencies = {}  # Start frequency count for the new word

        # Store frequency for the current article ID
        word_frequencies[article_id] = frequency

    # Output the last word frequencies
    if current_word is not None:
        for article_id, freq in word_frequencies.items():
            print(f"({current_word}, {article_id}, {freq})")

if __name__ == "__main__":
    reducer()
