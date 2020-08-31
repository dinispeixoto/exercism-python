def steps(number):

    if number < 1:
        raise ValueError("Error")

    even = lambda x: x / 2
    odd = lambda x: 3 * x + 1

    return 0 if number == 1 else 1 + steps(even(number) if number % 2 == 0 else odd(number))
