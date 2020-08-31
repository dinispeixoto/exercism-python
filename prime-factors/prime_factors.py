def factors(number):
    n = 2
    factors = []

    while number > 1:
        while number % n == 0:
            number /= n
            factors.append(n)
        n += 1
    
    return factors