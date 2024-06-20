import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

dataset="Hello Everyone. Welcome to this course. We are studying NLP."
print(sent_tokenize(text=dataset, language='english'))
print(word_tokenize(text=dataset, language='english'))
