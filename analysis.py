import pandas as pd
from nltk.corpus import wordnet as wn
import nltk
from rpy2 import robjects

r = robjects.r

str = """
library(networkD3)
data(MisLinks)
data(MisNodes)
a=forceNetwork(Links = MisLinks, Nodes = MisNodes,
             Source = "source", Target = "target",
             Value = "value", NodeID = "name",
             Group = "group", opacity = 0.8)
saveNetwork(a, 'D:/Github/Vocabulary_Analysis/net2.html')
"""

r(str)

# corpus = pd.read_csv('./ECDICT/ecdict.csv', sep=',', error_bad_lines=False, index_col=False, dtype='unicode')


def print_all_lemma(word):
    for i in wn.synsets(word):
        w = i
        print('{}'.format(w), w.lemma_names())

