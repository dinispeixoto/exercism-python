from functools import reduce

def largest_product(series, size):

    if size == 0:
        return 1

    if not series or len(series) < size or size < 0:
        raise ValueError("Error")

    largest = 0
    for number in slices(series, size):
        result = reduce(lambda x, y: x*y, [int(digit) for digit in number])
        if result > largest:
            largest = result
    return largest


def slices(series, length):
    return list(filter(lambda x: len(x) == length, [series[i:i + length] for i in range(len(series))]))