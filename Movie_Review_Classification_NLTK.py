import nltk
import random
from nltk.corpus import movie_reviews

documents=[]
for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        documents.append((list(movie_reviews.words(fileid)), category))

random.shuffle(documents)
# we shuffled as we are using same data for training & test, to avoid bias

all_words=[]
for w in movie_reviews.words():
   all_words.append(w.lower())

all_words=nltk.FreqDist(all_words)
print(all_words.most_common(15))

word_features=list(all_words.keys())[:3000]

def find_features(document):
    words=set(document)
    features={}
    for w in word_features:
        features[w]= (w in words)
    return features

print((find_features(movie_reviews.words('pos/cv005_29443.txt'))))
featuresets=[(find_features(rev),category) for (rev, category) in documents]
training_set=featuresets[:1900]
test_set=featuresets[1900:]

classifier=nltk.NaiveBayesClassifier.train(training_set)
print("Accuracy:", (nltk.classify.accuracy(classifier, test_set))*100)

classifier.show_most_informative_features(15)