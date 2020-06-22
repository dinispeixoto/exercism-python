ALLERGIES = {
    "eggs": 0,
    "peanuts": 1,
    "shellfish": 2,
    "strawberries": 3,
    "tomatoes": 4,
    "chocolate": 5,
    "pollen": 6,
    "cats": 7
}


class Allergies:
    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return (self.score >> ALLERGIES.get(item) & 1) != 0

    @property
    def lst(self):
        return [ item for item in ALLERGIES.keys() if self.allergic_to(item)]
