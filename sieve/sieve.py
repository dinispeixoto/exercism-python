def primes(limit):
    if limit < 2:
        return []

    numbers = range(2, limit + 1)
    for number in numbers:
        numbers = [
            prime for prime in numbers
            if prime % number != 0 or prime == number
        ]

    return numbers