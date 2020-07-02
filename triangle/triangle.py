def equilateral(sides):
    return is_valid_triangle(sides) and len(set(sides)) == 1


def isosceles(sides):
    return is_valid_triangle(sides) and not scalene(sides)


def scalene(sides):
    return is_valid_triangle(sides) and len(set(sides)) == 3


def is_valid_triangle(sides):
    return (
        sides[0] + sides[1] > sides[2] and
        sides[0] + sides[2] > sides[1] and
        sides[1] + sides[2] > sides[0]
    )
