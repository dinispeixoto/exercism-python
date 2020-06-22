from itertools import islice


def prime(number):
    return next(islice(prime_generator(), number - 1, None))

# Prime generator
def prime_generator():
    q, D = 2, {}

    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1
