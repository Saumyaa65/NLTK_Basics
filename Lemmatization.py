import nltk
from nltk.stem import WordNetLemmatizer

wnl=WordNetLemmatizer()
print(wnl.lemmatize('churches'))
print(wnl.lemmatize('dogs'))
print(wnl.lemmatize('feet'))
print(wnl.lemmatize('better', pos='a'))
# pos is part of speech, a means adjective, default is noun
# stemming does not have pos and only removes few letters from end while
#  lemmatization gets dictionary form of words
