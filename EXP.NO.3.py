import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
text = "The cats are running and the boys played football."
# Tokenization
words = word_tokenize(text)
print("Tokens:", words)
# POS tagging
tagged_words = nltk.pos_tag(words)
print("POS Tags:", tagged_words)
# Lemmatization
lemmatizer = WordNetLemmatizer()
for word in words:
    print(word, "->", lemmatizer.lemmatize(word))
