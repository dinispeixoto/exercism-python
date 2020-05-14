import re
from itertools import groupby


def count_words(sentence):
    sentence = [
        x.strip("'") for x in re.split("[^a-z0-9']+", sentence.lower()) if x
    ]

    return {
        word: len(list(group))
        for word, group in groupby(sorted(sentence))
    }
