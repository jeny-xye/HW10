"""
HW10
Author: XinYi Ye
Date: 11/01/2019
"""
import HW10_XinYi_Ye
import unittest


class TestMajor(unittest.TestCase):
    """ TestMajor class: test cases in HW10_XinYi_Ye """

    def test__init(self):
        """ test __init__() method """
        directory1 = 'SIT'
        m1 = HW10_XinYi_Ye.Major(directory1)
        directory2 = 'NYU'
        m2 = HW10_XinYi_Ye.Major(directory2)
        directory3 = ''
        m3 = HW10_XinYi_Ye.Major(directory3)
        self.assertTrue(m1.directory == directory1)
        self.assertTrue(m2.directory == directory2)
        self.assertTrue(m3.directory == directory3)
        self.assertTrue(m1.d_major == {})
        self.assertTrue(m2.d_major == {})
        self.assertTrue(m3.d_major == {})

    def test_get_majors(self):
        """ test get_majors() method """
        directory1 = 'NYU'
        m1 = HW10_XinYi_Ye.Major(directory1)
        result1 = {'SFEN': [['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], [
            'CS 501', 'CS 513', 'CS 545']]}
        self.assertTrue(m1.get_majors() == result1)
        with self.assertRaises(ValueError):
            """ in 'CU' directory, grades file has wrong fields """
            directory2 = 'CU'
            m2 = HW10_XinYi_Ye.Major(directory2)
            m2.get_majors()
        with self.assertRaises(FileNotFoundError):
            directory3 = 'jnn'
            m3 = HW10_XinYi_Ye.Major(directory3)
            m3.get_majors()


class TestGrades(unittest.TestCase):
    """ TestStudent class: test cases in HW10_XinYi_Ye """

    def test__init(self):
        """ test __init__() method """
        directory1 = 'SIT'
        m1 = HW10_XinYi_Ye.Grade(directory1)
        directory2 = 'NYU'
        m2 = HW10_XinYi_Ye.Grade(directory2)
        directory3 = ''
        m3 = HW10_XinYi_Ye.Grade(directory3)
        self.assertTrue(m1.directory == directory1)
        self.assertTrue(m2.directory == directory2)
        self.assertTrue(m3.directory == directory3)
        self.assertTrue(m1.l_grade == [])
        self.assertTrue(m2.l_grade == [])
        self.assertTrue(m3.l_grade == [])

    def test_get_grades(self):
        """ test get_grades() method """
        directory1 = 'NYU'
        m1 = HW10_XinYi_Ye.Grade(directory1)
        result1 = [['10103', 'SSW 567', 'A', '98765'], ['10103', 'SSW 564', 'A-', '98764'],
                   ['10103', 'SSW 687', 'B', '98764'], ['10103', 'CS 501', 'B', '98764']]
        self.assertTrue(m1.get_grades() == result1)
        with self.assertRaises(ValueError):
            """ in 'CU' directory, grades file has wrong fields """
            directory2 = 'CU'
            m2 = HW10_XinYi_Ye.Grade(directory2)
            m2.get_grades()
        with self.assertRaises(FileNotFoundError):
            directory3 = 'jnn'
            m3 = HW10_XinYi_Ye.Grade(directory3)
            m3.get_grades()


class TestStudent(unittest.TestCase):
    """ TestStudent class: test cases in HW10_XinYi_Ye """

    def test__init(self):
        """ test __init__() method """
        directory1 = 'SIT'
        m1 = HW10_XinYi_Ye.Student(directory1)
        directory2 = 'NYU'
        m2 = HW10_XinYi_Ye.Student(directory2)
        directory3 = ''
        m3 = HW10_XinYi_Ye.Student(directory3)
        self.assertTrue(m1.directory == directory1)
        self.assertTrue(m2.directory == directory2)
        self.assertTrue(m3.directory == directory3)
        self.assertTrue(m1.list_student == [])
        self.assertTrue(m2.list_student == [])
        self.assertTrue(m3.list_student == [])

    def test_student_operation(self):
        """ test student_operation() method """
        directory1 = 'NYU'
        m1 = HW10_XinYi_Ye.Student(directory1)
        result = [['10103', 'Baldwin, C', 'SFEN', [('CS 501', 'B'), ('SSW 564', 'A-'), ('SSW 567', 'A'), ('SSW 687', 'B')], [
            'CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], 'None']]
        self.assertTrue(m1.student_operation() == result)
        with self.assertRaises(ValueError):
            """ major in students file has wrong format """
            directory2 = 'CU'
            m2 = HW10_XinYi_Ye.Student(directory2)
            m2.student_operation()
        with self.assertRaises(FileNotFoundError):
            directory3 = 'jnn'
            m3 = HW10_XinYi_Ye.Student(directory3)
            m3.student_operation()


class TestInstructor(unittest.TestCase):
    """ TestInstructor class: test cases in HW10_XinYi_Ye """

    def test__init(self):
        """ test __init__() method """
        directory1 = 'SIT'
        m1 = HW10_XinYi_Ye.Instructor(directory1)
        directory2 = 'NYU'
        m2 = HW10_XinYi_Ye.Instructor(directory2)
        directory3 = ''
        m3 = HW10_XinYi_Ye.Instructor(directory3)
        self.assertTrue(m1.directory == directory1)
        self.assertTrue(m2.directory == directory2)
        self.assertTrue(m3.directory == directory3)
        self.assertTrue(m1.list_instructor == [])
        self.assertTrue(m2.list_instructor == [])
        self.assertTrue(m3.list_instructor == [])

    def test_instructor_operation(self):
        """ test instructor_operation() method """
        directory1 = 'NYU'
        m1 = HW10_XinYi_Ye.Instructor(directory1)
        result = [['98765', 'Einstein, A', 'SFEN', {'SSW 567': 1}], [
            '98764', 'Feynman, R', 'SFEN', {'SSW 564': 1, 'SSW 687': 1, 'CS 501': 1}]]
        self.assertTrue(m1.instructor_operation() == result)
        with self.assertRaises(ValueError):
            """ insturctors file in CU doesn't have header line """
            directory2 = 'CU'
            m2 = HW10_XinYi_Ye.Instructor(directory2)
            m2.instructor_operation()
        with self.assertRaises(FileNotFoundError):
            directory3 = 'jnn'
            m3 = HW10_XinYi_Ye.Instructor(directory3)
            m3.instructor_operation()


class TestRepository(unittest.TestCase):
    """ TestRepository class: test cases in HW10_XinYi_Ye """

    def test__init(self):
        """ test __init__() method """
        directory1 = 'SIT'
        m1 = HW10_XinYi_Ye.Repository(directory1)
        directory2 = 'NYU'
        m2 = HW10_XinYi_Ye.Repository(directory2)
        directory3 = ''
        m3 = HW10_XinYi_Ye.Repository(directory3)
        self.assertTrue(m1.directory == directory1)
        self.assertTrue(m2.directory == directory2)
        self.assertTrue(m3.directory == directory3)
        self.assertTrue(m1.stu == {})
        self.assertTrue(m2.stu == {})
        self.assertTrue(m3.stu == {})
        self.assertTrue(m1.ins == {})
        self.assertTrue(m2.ins == {})
        self.assertTrue(m3.ins == {})
        self.assertTrue(m1.maj == {})
        self.assertTrue(m2.maj == {})
        self.assertTrue(m3.maj == {})

    def test_repository_operation(self):
        """ test instructor_operation() method """
        directory1 = 'NYU'
        m1 = HW10_XinYi_Ye.Repository(directory1)
        a, b, c = m1.repository_operation()
        result1 = {'SFEN': [['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'],
                            ['CS 501', 'CS 513', 'CS 545']]}
        result2 = {'10103': ['10103', 'Baldwin, C', 'SFEN', [('CS 501', 'B'), ('SSW 564', 'A-'), ('SSW 567', 'A'), ('SSW 687', 'B')],
                             ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], 'None']}
        result3 = {'98765': ['98765', 'Einstein, A', 'SFEN', {'SSW 567': 1}], '98764':
                   ['98764', 'Feynman, R', 'SFEN', {'SSW 564': 1, 'SSW 687': 1, 'CS 501': 1}]}
        self.assertTrue(a == result1)
        self.assertTrue(b == result2)
        self.assertTrue(c == result3)
        with self.assertRaises(ValueError):
            directory2 = 'CU'
            m2 = HW10_XinYi_Ye.Repository(directory2)
            m2.repository_operation()
        with self.assertRaises(FileNotFoundError):
            directory4 = 'JUU'
            m4 = HW10_XinYi_Ye.Repository(directory4)
            m4.repository_operation()


if __name__ == "__main__":
    """ main function """
    unittest.main(exit=False, verbosity=2)
