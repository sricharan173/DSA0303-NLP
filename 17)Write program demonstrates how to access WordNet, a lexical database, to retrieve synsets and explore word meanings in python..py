import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet

def get_word_meanings(word):
    synsets = wordnet.synsets(word)

    if not synsets:
        print(f"No meanings found for '{word}'")
    else:
        print(f"Meanings for '{word}':")
        for synset in synsets:
            print(f"Synset: {synset.name()}")
            print(f"Definition: {synset.definition()}")
            print(f"Examples: {', '.join(synset.examples())}")
            print()

if __name__ == "__main__":
    while True:
        word = input("Enter a word (or 'q' to quit): ")
        if word.lower() == 'q':
            break
        get_word_meanings(word)
