SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif all(item in list_two for item in list_one):
        return SUBLIST
    elif all(item in list_one for item in list_two):
        return SUPERLIST
    else:
        return UNEQUAL
