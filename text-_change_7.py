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

# Number of words
word_count = len(filtered_words)

# Number of sentences
sentence_count = len(sentences)

# Number of paragraphs
paragraph_count = text.count('\n\n') + 1

# The number of each English vowel
vowels = "aeiou"
vowel_counts = {vowel: 0 for vowel in vowels}
for char in text:
    if char in vowels:
        vowel_counts[char] += 1

# Number of silent letters
consonant_count = sum(char not in vowels for char in text if char.isalnum())

# Variance of the number of vowels in each sentence
sentence_vowel_counts = [sum(char in vowels for char in sentence if char.isalnum()) for sentence in sentences]
sentence_vowel_variance = np.var(sentence_vowel_counts)

# Variance of the number of vowels in each paragraph
paragraph_vowel_counts = []
for paragraph in text.split('\n\n'):
    paragraph_vowel_counts.append(sum(char in vowels for char in paragraph if char.isalnum()))
paragraph_vowel_variance = np.var(paragraph_vowel_counts)

# Variance of the number of vowels in the whole text
total_vowel_count = sum(char in vowels for char in text if char.isalnum())
total_vowel_variance = np.var([total_vowel_count])

