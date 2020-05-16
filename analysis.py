import pandas as pd
from nltk.corpus import wordnet as wn
import nltk
from rpy2 import robjects

def R_network_plot(data, map_name):
    r = robjects.r
    MisLinks, MisNodes = data

    str = """
    library(networkD3)
    data({})
    data({})
    a=forceNetwork(Links = MisLinks, Nodes = MisNodes,
                Source = "source", Target = "target",
                Value = "value", NodeID = "name",
                Group = "group", opacity = 0.8)
    saveNetwork(a, 'D:/Github/Vocabulary_Analysis/Map/{}.html')
    """.format(MisLinks, MisNodes, map_name)
    r(str)

# corpus = pd.read_csv('./ECDICT/ecdict.csv', sep=',', error_bad_lines=False, index_col=False, dtype='unicode')


def print_all_lemma(word):
    for i in wn.synsets(word):
        w = i
        print('{}'.format(w), w.lemma_names())

if __name__=='__main__':
    print_all_lemma('emphasize')



