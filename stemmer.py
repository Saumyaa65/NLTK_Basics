import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

dataset=['love', 'loving', 'lover', 'loved', 'lovingly', 'loves', 'lovely']
ps=PorterStemmer()
for i in dataset:
    print(ps.stem(i))

dataset2=("It feels very special when you are loving someone. "
          "We care for our loved ones. "
          "Specially when we love each other unconditionally.")
words=word_tokenize(dataset2)
for w in words:
    print(ps.stem(w))