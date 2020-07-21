def find(input, value):
    min, max = 0, len(input) - 1

    while min <= max:
        index = (min + max) // 2
        if input[index] == value:
            return index
        elif value < input[index]:
            max = index - 1
        else:
            min = index + 1

    raise ValueError("Not found")
