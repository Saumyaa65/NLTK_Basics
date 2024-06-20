import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

dataset=("Hello Mr. Watson, how are you doing today? "
         "The weather is awesome. The garden is Green. "
         "We should go out for a walk.")
dataset=dataset.lower()
stop_words=set(stopwords.words('english'))
print(stop_words)
word_tokenize=word_tokenize(dataset)
filtered_sentences=[]
for w in word_tokenize:
    if w not in stop_words:
        filtered_sentences.append(w)
print(filtered_sentences)