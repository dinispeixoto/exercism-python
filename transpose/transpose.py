from itertools import zip_longest


def transpose(lines):
    lines = lines.split("\n")
    return '\n'.join([process_tuple(tuple) for tuple in zip_longest(*lines)])


def process_tuple(tuple):
    if None in tuple:
        print(tuple)
        tuple = ''.join([
            element if element is not None else ' ' for element in tuple
        ]).rstrip()

    return ''.join(tuple)
