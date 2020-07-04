# WIP: really ugly

def rows(letter):
    distance = 2 * (ord(letter) - ord('A')) - 1

    if distance < 0:
        return ['A']

    half_diamond = generate_half_diamond(previous_letter(letter), distance - 1,
                                         distance)

    return half_diamond + [letter + n_spaces(distance) + letter
                           ] + half_diamond[::-1]


def generate_half_diamond(letter, distance, max_distance):
    outside = max_distance - distance
    inside = max_distance - 2 * outside

    if inside < 1:
        return [n_spaces(outside) + letter + n_spaces(outside)]
    else:
        inside_letter = letter + n_spaces(inside) + letter

        return generate_half_diamond(
            previous_letter(letter), distance - 1, max_distance) + [
                n_spaces(outside) + inside_letter + n_spaces(outside)
            ]


def previous_letter(letter):
    return chr(ord(letter) - 1)


def n_spaces(size):
    return ' ' * size