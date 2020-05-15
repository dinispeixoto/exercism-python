
scores = {
    1: 'aeioulnrst',
    2: 'dg',
    3: 'bcmp',
    4: 'fhvwy',
    5: 'k',
    8: 'jx',
    10: 'qz'
}


def score(word):
    return sum(sum([list(filter(lambda key: letter in scores[key], scores.keys())) for letter in word.lower()], []))
