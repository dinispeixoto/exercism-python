"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

from collections import Counter

YACHT = (lambda dice: 50 if len(set(dice)) == 1 else 0)
ONES = (lambda dice: number_of_digits(dice, 1))
TWOS = (lambda dice: number_of_digits(dice, 2))
THREES = (lambda dice: number_of_digits(dice, 3))
FOURS = (lambda dice: number_of_digits(dice, 4))
FIVES = (lambda dice: number_of_digits(dice, 5))
SIXES = (lambda dice: number_of_digits(dice, 6))
FULL_HOUSE = (lambda dice: sum(dice)
              if sorted(Counter(dice).values()) == [2, 3] else 0)
FOUR_OF_A_KIND = (lambda dice: four_of_a_kind(dice))
LITTLE_STRAIGHT = (lambda dice: 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0)
BIG_STRAIGHT = (lambda dice: 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0)
CHOICE = (lambda dice: sum(dice))


def number_of_digits(dice, digit):
    return digit * dice.count(digit)


def four_of_a_kind(dice):
    four_times_elements = [
        n_dice for n_dice in set(dice) if dice.count(n_dice) >= 4
    ]
    return 4 * four_times_elements[0] if len(four_times_elements) > 0 else 0


def score(dice, category):
    return category(dice)
