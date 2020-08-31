def square(number):
    if number <= 0 or number > 64:
        raise ValueError("Error")

    return 1 << (number - 1)


def total():
    return (1 << 64) - 1