SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def tuples(list):
    return [(list[i], list[i + 1]) for i in range(len(list) - 1)]


def is_sublist(list_one, list_two):
    return all(item in list_two for item in list_one) and all(item in tuples(list_two) for item in tuples(list_one))


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif is_sublist(list_one, list_two):
        return SUBLIST
    elif is_sublist(list_two, list_one):
        return SUPERLIST
    else:
        return UNEQUAL
