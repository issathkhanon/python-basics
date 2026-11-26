"""One student's mark book.

MarkBook("Issath") starts with an empty list.
add stores one mark from 0 to 100 and raises ValueError otherwise.
total adds the stored marks.
passed is True when the average mark is 50 or more.
"""


class MarkBook:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def add(self, mark):
        if mark < 0 or mark > 100:
            raise ValueError("a mark is from 0 to 100")
        self.marks.append(mark)

    def total(self):
        return sum(self.marks)

    def passed(self):
        if not self.marks:
            return False
        average = self.total() / len(self.marks)
        return average >= 50
