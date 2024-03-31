#!/usr/bin/env python3

import sys
import math

def reducer():
    word_frequencies = {}  #dictionary to store word frequencies across articles
    total_documents = 0  # total number of documents
    
    for line in sys.stdin:
        word_id, freq_info = line.strip().split('\t')
        article_id, frequency = freq_info.split(':')
        article_id = int(article_id)
        frequency = int(frequency)
        
        #aggregate word frequencies per article
        if word_id not in word_frequencies:
            word_frequencies[word_id] = {}
        word_frequencies[word_id][article_id] = word_frequencies[word_id].get(article_id, 0) + frequency
        total_documents = max(total_documents, article_id)  # update total documents count

    #IDF values
    idf_values = {term_id: math.log(total_documents / (len(freq_dict) + 1)) for term_id, freq_dict in word_frequencies.items()}

    #TF-IDF scores
    tfidf_scores = {}
    for word_id, freq_dict in word_frequencies.items():
        tfidf_scores[word_id] = {}
        for article_id, frequency in freq_dict.items():
            idf = idf_values.get(word_id, 0)
            tfidf = frequency * idf
            tfidf_scores[word_id][article_id] = round(tfidf, 2)

    #output TF-IDF scores
    for word_id, scores in sorted(tfidf_scores.items(), key=lambda x: int(x[0])):
        for article_id, score in sorted(scores.items(), key=lambda x: int(x[0])):
            print(f"{word_id}\t{article_id}\t{score}")  # emit word ID, article ID, and TF-IDF score

if __name__ == "__main__":
    reducer()

