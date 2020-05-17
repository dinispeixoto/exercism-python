import re


def abbreviate(words):
    return ''.join([word[0] for word in re.split("[-_, ]", words.upper()) if word])
