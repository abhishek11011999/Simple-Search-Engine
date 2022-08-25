# Add your import statements here

import nltk
from nltk.corpus import wordnet
nltk.download('averaged_perceptron_tagger')




def pos_tagger(nltk_tag):
        if nltk_tag.startswith('J'):
            return wordnet.ADJ
        elif nltk_tag.startswith('V'):
            return wordnet.VERB
        elif nltk_tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN

def RelDocs(qrels):
    true_docs_all = dict()

    for i in qrels:
        if int(i["query_num"]) not in true_docs_all.keys():
            true_docs_all[int(i["query_num"])] = []
            
        true_docs_all[int(i["query_num"])].append(int(i['id']))
    return true_docs_all

# Add any utility functions here