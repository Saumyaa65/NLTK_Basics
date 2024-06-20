import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

dataset=("Taj Mahal is one of the world's most celebrated structures."
         "It is a stunning symbol of Indian rich history.")
new_dataset=word_tokenize(dataset)
print(pos_tag(new_dataset))
# print(nltk.help.upenn_tagset()) for list of pos tags
