class School:
    def __init__(self):
        self._roster = {}

    def add_student(self, name, grade):
        self._roster[grade] = self._roster.get(grade, []) + [name]

    def roster(self):
        return [
            element for key in sorted(self._roster.keys())
            for element in sorted(self._roster[key])
        ]

    def grade(self, grade_number):
        return sorted(self._roster.get(grade_number, []))
