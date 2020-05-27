DEFAULT_STUDENTS = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]

PLANTS = {
    "G": "Grass",
    "C": "Clover",
    "V": "Violets",
    "R": "Radishes",
}


class Garden:
    def __init__(self, diagram, students = DEFAULT_STUDENTS):
        self.studens = sorted(students)
        self.garden = diagram.split("\n")

    def plants(self, student):
        index = self.studens.index(student)
        first, second = (index * 2), (index * 2) + 1

        return [
            PLANTS[self.garden[0][first]],
            PLANTS[self.garden[0][second]],
            PLANTS[self.garden[1][first]],
            PLANTS[self.garden[1][second]],
        ]

    # def _generate_plants(self, diagram, students):
    #     plants = diagram.split("\n")

    #     index = 0
    #     garden = {}

    #     for (plant_a, plant_b) in zip(*plants):
    #         students[index] = [plant_a, plant_b]    

    #     return garden



