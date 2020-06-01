def is_valid(isbn):
    isbn = isbn.replace("-","")

    result = 0
    multiplier = 10
    for value in isbn:
        if value.isalpha():
            if value == "X":
                result+=10*multiplier
            else:
                return False
        else:
            result+=int(value)*multiplier
        multiplier-=1

    return (result%11) == 0
