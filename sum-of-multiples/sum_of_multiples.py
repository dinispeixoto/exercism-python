def sum_of_multiples(limit, multiples):
    return sum(
        set([
            number for multiple in multiples for number in range(1, limit)
            if multiple and number % multiple == 0
        ]))
