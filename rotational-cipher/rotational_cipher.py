def rotate(text, key):
    return ''.join([rotate_letter(letter, key) for letter in text])


def rotate_letter(letter, key):
    base = ord('A') if letter.isupper() else ord('a')
    return chr(base + (ord(letter) - base + key) % 26) if letter.isalpha() else letter
