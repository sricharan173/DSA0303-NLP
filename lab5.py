import nltk
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = ["running", "flies", "happily", "stemming", "beautifully", "jumps"]
stemmed_words = [stemmer.stem(word) for word in words]
for original, stemmed in zip(words, stemmed_words):
    print(f"{original} -> {stemmed}")
