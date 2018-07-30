import unittest

from grading_students import grade_students

class GradingStudentsTestCase(unittest.TestCase):
    def test_should_not_round_38(self):
        grades = [38]
        expected = [40]

        self.assertEquals(expected, grade_students(grades))
        
    def test_should_not_round_37(self):
        grades = [37]
        expected = [37]

        self.assertEquals(expected, grade_students(grades))
        
    def test_should_round_39_to_40(self):
        grades = [39]
        expected = [40]

        self.assertEquals(expected, grade_students(grades))
        
    def test_should_not_round_40(self):
        grades = [40]
        expected = [40]

        self.assertEquals(expected, grade_students(grades))
        
    def test_should_round_grades(self):
        grades = [41, 42, 43, 44, 45, 97, 98, 99, 100]
        expected = [41, 42, 45, 45, 45, 97, 100, 100, 100]

        self.assertEquals(expected, grade_students(grades))
        