"""
HW09
Author: XinYi Ye
Date: 11/01/2019
"""
from collections import defaultdict
import HW09_XinYi_Ye
import unittest


class TestGrade(unittest.TestCase):
    """ TestGrade class: test cases in HW09_XinYi_Ye """

    def test__init(self):
        """ test __init__() method """
        directory1 = 'SIT'
        m1 = HW09_XinYi_Ye.Grade(directory1)
        directory2 = 'NYU'
        m2 = HW09_XinYi_Ye.Grade(directory2)
        directory3 = ''
        m3 = HW09_XinYi_Ye.Grade(directory3)
        self.assertTrue(m1.directory == directory1)
        self.assertTrue(m2.directory == directory2)
        self.assertTrue(m3.directory == directory3)
        self.assertTrue(m1.l_grade == [])
        self.assertTrue(m2.l_grade == [])
        self.assertTrue(m3.l_grade == [])

    def test_get_grades(self):
        """ test get_grades() method """
        directory1 = 'NYU'
        m1 = HW09_XinYi_Ye.Grade(directory1)
        result1 = [['10103', 'SSW 567', 'A', '98765'], ['10103', 'SSW 564', 'A-', '98764'],
                   ['10103', 'SSW 687', 'B', '98764'], [
                       '10103', 'CS 501', 'B', '98764'],
                   ['10172', 'SSW 555', 'A', '98763'], ['10172', 'SSW 567', 'A-', '98765']]
        self.assertTrue(m1.get_grades() == result1)
        with self.assertRaises(ValueError):
            """ in 'CU' directory, grades file has wrong fields """
            directory2 = 'CU'
            m2 = HW09_XinYi_Ye.Grade(directory2)
            m2.get_grades()
        with self.assertRaises(FileNotFoundError):
            directory3 = 'jnn'
            m3 = HW09_XinYi_Ye.Grade(directory3)
            m3.get_grades()


class TestStudent(unittest.TestCase):
    """ TestStudent class: test cases in HW09_XinYi_Ye """

    def test__init(self):
        """ test __init__() method """
        directory1 = 'SIT'
        m1 = HW09_XinYi_Ye.Student(directory1)
        directory2 = 'NYU'
        m2 = HW09_XinYi_Ye.Student(directory2)
        directory3 = ''
        m3 = HW09_XinYi_Ye.Student(directory3)
        self.assertTrue(m1.directory == directory1)
        self.assertTrue(m2.directory == directory2)
        self.assertTrue(m3.directory == directory3)
        self.assertTrue(m1.list_student == [])
        self.assertTrue(m2.list_student == [])
        self.assertTrue(m3.list_student == [])

    def test_student_operation(self):
        """ test student_operation() method """
        directory1 = 'NYU'
        m1 = HW09_XinYi_Ye.Student(directory1)
        result = [['10103', 'Baldwin, C', 'SFEN', {'CS 501': 'B', 'SSW 564': 'A-', 'SSW 567': 'A', 'SSW 687': 'B'}],
                  ['10172', 'Forbes, I', 'SFEN', {'SSW 555': 'A', 'SSW 567': 'A-'}]]
        self.assertTrue(m1.student_operation() == result)
        with self.assertRaises(ValueError):
            directory2 = 'CU'
            m2 = HW09_XinYi_Ye.Student(directory2)
            m2.student_operation()
        with self.assertRaises(FileNotFoundError):
            directory3 = 'jnn'
            m3 = HW09_XinYi_Ye.Student(directory3)
            m3.student_operation()


class TestInstructor(unittest.TestCase):
    """ TestInstructor class: test cases in HW09_XinYi_Ye """

    def test__init(self):
        """ test __init__() method """
        directory1 = 'SIT'
        m1 = HW09_XinYi_Ye.Instructor(directory1)
        directory2 = 'NYU'
        m2 = HW09_XinYi_Ye.Instructor(directory2)
        directory3 = ''
        m3 = HW09_XinYi_Ye.Instructor(directory3)
        self.assertTrue(m1.directory == directory1)
        self.assertTrue(m2.directory == directory2)
        self.assertTrue(m3.directory == directory3)
        self.assertTrue(m1.list_instructor == [])
        self.assertTrue(m2.list_instructor == [])
        self.assertTrue(m3.list_instructor == [])

    def test_instructor_operation(self):
        """ test instructor_operation() method """
        directory1 = 'NYU'
        m1 = HW09_XinYi_Ye.Instructor(directory1)
        result = [['98765', 'Einstein, A', 'SFEN', {'SSW 567': 2}], ['98764', 'Feynman, R', 'SFEN', {
            'SSW 564': 1, 'SSW 687': 1, 'CS 501': 1}], ['98763', 'Newton, I', 'SFEN', {'SSW 555': 1}]]
        self.assertTrue(m1.instructor_operation() == result)
        with self.assertRaises(ValueError):
            directory2 = 'CU'
            m2 = HW09_XinYi_Ye.Instructor(directory2)
            m2.instructor_operation()
        with self.assertRaises(FileNotFoundError):
            directory3 = 'jnn'
            m3 = HW09_XinYi_Ye.Instructor(directory3)
            m3.instructor_operation()


class TestRepository(unittest.TestCase):
    """ TestRepository class: test cases in HW09_XinYi_Ye """

    def test__init(self):
        """ test __init__() method """
        directory1 = 'SIT'
        m1 = HW09_XinYi_Ye.Repository(directory1)
        directory2 = 'NYU'
        m2 = HW09_XinYi_Ye.Repository(directory2)
        directory3 = ''
        m3 = HW09_XinYi_Ye.Repository(directory3)
        self.assertTrue(m1.directory == directory1)
        self.assertTrue(m2.directory == directory2)
        self.assertTrue(m3.directory == directory3)
        self.assertTrue(m1.stu == {})
        self.assertTrue(m2.stu == {})
        self.assertTrue(m3.stu == {})
        self.assertTrue(m1.ins == {})
        self.assertTrue(m2.ins == {})
        self.assertTrue(m3.ins == {})

    def test_repository_operation(self):
        """ test instructor_operation() method """
        directory1 = 'NYU'
        m1 = HW09_XinYi_Ye.Repository(directory1)
        a, b = m1.repository_operation()
        result1 = {'10103': ['10103', 'Baldwin, C', 'SFEN', {'CS 501': 'B', 'SSW 564': 'A-', 'SSW 567': 'A', 'SSW 687': 'B'}],
                   '10172': ['10172', 'Forbes, I', 'SFEN', {'SSW 555': 'A', 'SSW 567': 'A-'}]}
        result2 = {'98765': ['98765', 'Einstein, A', 'SFEN', {'SSW 567': 2}],
                   '98764': ['98764', 'Feynman, R', 'SFEN', {'SSW 564': 1, 'SSW 687': 1, 'CS 501': 1}],
                   '98763': ['98763', 'Newton, I', 'SFEN', {'SSW 555': 1}]}
        self.assertTrue(a == result1)
        self.assertTrue(b == result2)
        with self.assertRaises(ValueError):
            directory2 = 'CU'
            m2 = HW09_XinYi_Ye.Repository(directory2)
            m2.repository_operation()
        with self.assertRaises(FileNotFoundError):
            directory4 = 'JUU'
            m4 = HW09_XinYi_Ye.Repository(directory4)
            m4.repository_operation()


if __name__ == "__main__":
    """ main function """
    unittest.main(exit=False, verbosity=2)
