def triplets_with_sum(number):
    triplets = []

    for a in range(1, number):
        for b in range(a + 1, number):
            c = number - a - b
            if c < b:
                break
            
            triplet = [a, b, c]
            if is_triplet(triplet):
                triplets.append(triplet)
    return triplets


def triplets_in_range(start, end):
    pass


def is_triplet(triplet):
    a, b, c = triplet
    return a**2 + b**2 == c**2
