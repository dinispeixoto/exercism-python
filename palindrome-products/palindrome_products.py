def palindrome_factors(min_factor, max_factor):

    palindrome_factors = {}

    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            if is_palindrome(i * j):
                palindrome_factors.setdefault(i * j, []).append([i, j])

    return palindrome_factors


def largest(min_factor, max_factor):

    if max_factor < min_factor:
        raise ValueError("Max factor is lower than min factor.")

    factors = palindrome_factors(min_factor, max_factor)
    sorted_factors = sorted(factors.keys(), reverse=True)
    largest_factor = sorted_factors[0] if sorted_factors else None

    return largest_factor, factors.get(largest_factor, [])


def smallest(min_factor, max_factor):

    if max_factor < min_factor:
        raise ValueError("Max factor is lower than min factor.")

    factors = palindrome_factors(min_factor, max_factor)
    sorted_factors = sorted(factors.keys())
    lower_factor = sorted_factors[0] if sorted_factors else None

    return lower_factor, factors.get(lower_factor, [])


def is_palindrome(number):
    return str(number) == str(number)[::-1]