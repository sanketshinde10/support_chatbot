import nltk
nltk.download('punkt_tab')
from nltk.stem import PorterStemmer
import numpy as np
import json
import pickle
import os

stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    return np.array([1 if w in tokenized_sentence else 0 for w in all_words])
