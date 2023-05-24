import json
import numpy as np
import torch
from flask import Flask, request, jsonify
import pandas as pd
from sentence_transformers import SentenceTransformer, util
import spacy
import re
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer



app = Flask(__name__)


# Precompile the regular expression pattern
CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

# Spacy stopwords
sp = spacy.load('en_core_web_sm')
all_stopwords = sp.Defaults.stop_words
all_stopwords.update({'&', ',', '.', '@', '/', ':', '?'})

# Preprocess the text to remove stopwords, punctuation, and lemmatize the tokens
def preprocess(text):
    # Tokenize the text into individual words
    tokens = word_tokenize(text)
    
    # Lowercase the tokens
    tokens = [token.lower() for token in tokens]
    
    # Remove special characters and punctuation
    tokens = [token.translate(str.maketrans('', '', string.punctuation)) for token in tokens]
    
    # Remove stopwords
    tokens = [token for token in tokens if token not in all_stopwords]
    
    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Join the tokens back into a single string
    preprocessed_text = ' '.join(tokens)
    
    # Remove HTML tags and entities
    preprocessed_text = re.sub(CLEANR, '', preprocessed_text)
    
    return preprocessed_text


clothing_data = pd.read_csv('data/preprocessed_data.csv')
model = SentenceTransformer('sentence-transformers/nli-distilroberta-base-v2')
embeddings = np.load('data/embeddings.npy')


# Return ranked results
def get_recomended_items(input_text, top_k=5):
    
    # Encode the query text
    query_embedding = model.encode([input_text], convert_to_tensor=True)
    # Compute similarity scores
    similarity_scores = util.pytorch_cos_sim(query_embedding, embeddings)[0]
    # Sort indices based on similarity scores
    sorted_indices = similarity_scores.argsort(descending=True)
    # Get the top-k most similar indices
    similar_indices = sorted_indices[:top_k].cpu().numpy()
    # Get the URLs of the top-k similar items
    similar_urls = clothing_data.loc[similar_indices, 'url'].tolist()
    for i in similar_urls:
        print(i)

    return similar_urls



@app.route('/', methods=['GET', 'POST'])
def clothing_similarity_search():
    try:
        data = request.get_json()

        input_text = data['text']
        n = data['N']
        n = int(n)
        recomended_items = get_recomended_items(input_text, n)

        response = {'recomended_items': recomended_items}
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
