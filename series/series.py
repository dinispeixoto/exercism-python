from textwrap import wrap


def slices(series, length):
    if not series or length <= 0 or length > len(series):
        raise ValueError("Error")

    return list(filter(lambda x: len(x) == length, [series[i:i + length] for i in range(len(series))]))
