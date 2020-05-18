DEFAULT_STUDENTS = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]

PLANTS = {
    "G": "Grass",
    "C": "Clover",
    "V": "Violets",
    "R": "Radishes",
}


class Garden:
    def __init__(self, diagram, students = DEFAULT_STUDENTS):
        self.garden = self._generate_plants(diagram, students)

    def plants(self, student):
        return [PLANTS[plant] for plant in self.garden[student]]

    def _generate_plants(self, diagram, students):
        plants = diagram.split("\n")

        index = 0
        garden = {}

        for (plant_a, plant_b) in zip(*plants):
            students[index] = [plant_a, plant_b]    

        return garden



