def is_isogram(string):
    filtered_string = ''.join(letter for letter in string.lower() if letter.isalpha())
    return len(set(filtered_string)) == len(filtered_string)
    
