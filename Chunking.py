import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import RegexpParser

dataset=("Taj Mahal is one of the world's most celebrated structures."
         "It is a stunning symbol of Indian rich history.")
new_dataset=word_tokenize(dataset)
pos_tagging=pos_tag(new_dataset)
print(pos_tagging)
sequence_chunk="""
chunk:
    {<NNPS>+}
    {<NNP>+}
    {<NN>+}
"""
chunk=RegexpParser(sequence_chunk)
chunk_result=chunk.parse(pos_tagging)
print(chunk_result)
