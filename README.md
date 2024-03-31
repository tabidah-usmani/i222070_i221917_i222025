# INTRODUCTION 

This repository contains a search application that has a dataset of 5 GB. A search engine retrieves and displays relevant information from a vast database of indexed documents in response to user queries. It employs algorithms to rank the retrieved results based on relevance, popularity, and other factors

# OUR WORKING
The preprocessing techniques involved in preparing text data for analysis entail several key steps. Firstly, tokenization divides the text into individual words or tokens, ensuring that each component is separated for analysis. Lowercasing normalizes the text by converting all tokens to lowercase, avoiding discrepancies due to capitalization. Removing punctuation aids in simplifying the text, eliminating unnecessary characters that could interfere with analysis. Finally, lemmatization reduces tokens to their base forms, aiding in standardization and reducing redundancy. By applying these techniques, the text is cleaned and prepared for further processing, such as assigning unique IDs to terms and calculating term frequencies per document, facilitating precise and accurate analysis.

# DOCUMENT INDEXING
Our first approach was to assign a unique ID to each term in the article

# FILES
```mapper.py```:The csv file is being read and sectences are tokenized to create a list <br> 
```reducer.py```: <br>
```example.csv```: the file consists of 2 columns that are Article ID and Section Text which are used for further analysis.


# CONTRIBUTORS
Maryam Khalid (22i-1917) <br>
Amna Javaid (22i-2025)
