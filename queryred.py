#!/usr/bin/env python3

import sys

#for each word in the query, the script calculates its tf by dividing its count by the total number of words in the query. The tf values are stored in the tf_values dictionary.

def query_reducer():
    word_counts = {}  
    total_words = 0  
    
    for line in sys.stdin:
        word, count = line.strip().split('\t')
        count = int(count)
        word_counts[word] = count
        total_words += count

#TF-IDF vector as a list of zeros with a length equal to the number of unique words in the query
    tf_values = {word: count / total_words for word, count in word_counts.items()}
    
    
    tfidf_vector = [0] * len(word_counts)

#it iterates over the tf_values dictionary to assign tf/idf values to the corresponding indices in the tf/idf vector based on the word ID mapping   
    word_id_mapping = {word: idx for idx, word in enumerate(sorted(word_counts.keys()))}
    for word, tf in tf_values.items():
        tfidf_vector[word_id_mapping[word]] = tf
    
    print(tfidf_vector)

if __name__ == "__main__":
    query_reducer()
