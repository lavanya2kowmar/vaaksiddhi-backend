import nltk

try:
    nltk.data.find("taggers/averaged_perceptron_tagger_eng")
except LookupError:
    nltk.download("averaged_perceptron_tagger_eng")

try:
    nltk.data.find("corpora/cmudict")
except LookupError:
    nltk.download("cmudict")