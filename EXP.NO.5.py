from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = [
    "playing",
    "played",
    "plays",
    "connected",
    "connecting",
    "connection",
    "studies",
    "studying",
    "happiness"
]
print("Original Word -> Stemmed Word")
for word in words:
    print(word, "->", stemmer.stem(word))
