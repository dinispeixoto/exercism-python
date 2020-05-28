def is_pangram(sentence):
    return len(set(''.join(filter(str.isalpha, sentence)).lower())) == 26
