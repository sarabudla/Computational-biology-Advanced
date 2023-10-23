#!/usr/bin/env python
# basic_classes.py

# creating the class "Circle"
# Fields:
# color (string), and
# radius (float)
class Circle:
    def __init__(self, color, radius):
        self.color = color
        self.radius = radius

    # Methods
    # diameter() which calculates the diameter of the circle (you can use math.pi or just 3.14)
    def diameter(self):
        return 2 * self.radius

    # circumfrence() which calculates the circumference of the circle.

    def circumfrence(self):
        return 2 * 3.14 * self.radius

    # isRed() which returns True if this circle is red.

    def isRed(self):
        if self.color == "red":
            return True


Circle_1 = Circle("red", 2.5)

print(Circle_1.color)
print(Circle_1.radius)
print(Circle_1.diameter())
print(Circle_1.circumfrence())
print(Circle_1.isRed())


# Creating the class "GraduateStudent"

class GraduateStudent:
    # Fields
    def __init__(self, first_name, last_name, year, major):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.major = major

    # Method
    # year_matriculated() which, given that it is January 2020, returns the year that the student began studying.
    # So, if the student's year is 1, then year_matriculated() should return 2019. If their year is 5,
    # then year_matriculated() should return 2015.

    def year_matriculated(self):
        return 2020 - self.year


test = GraduateStudent("jay", "ram", 5, "CS")
print(f"year matriculated is {test.year_matriculated()}")
