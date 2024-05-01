import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import spacy
from spacy import displacy

#  get text file 
with open('input.txt', encoding='utf-8') as f:
    text = f.read()

text = text.lower()  # change text to lowwercase
text = re.sub(r'[^\w\s]', '', text)  # Delete everything that is not text

sentences = sent_tokenize(text)
words = word_tokenize(text)

stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]

# Number of repetitions of each letter and number
char_counts = {}
for char in text:
    if char.isalnum():
        char_counts[char] = char_counts.get(char, 0) + 1
