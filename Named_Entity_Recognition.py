import numpy
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

dataset=("Abraham Lincoln was an American statesman and lawyer who served as "
         "the 16th President of the United States.")
dataset_tag= pos_tag(word_tokenize(dataset))
dataset_ner = ne_chunk(dataset_tag)
print(dataset_ner)

dataset_ner.draw()
