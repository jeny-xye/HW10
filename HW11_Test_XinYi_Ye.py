"""
HW11
Author: XinYi Ye
Date: 11/01/2019
"""
import HW11_XinYi_Ye
import unittest


class TestMajor(unittest.TestCase):
    """ TestMajor class: test cases in HW11_XinYi_Ye """

    def test__init(self):
        """ test __init__() method """
        directory1 = 'SIT'
        m1 = HW11_XinYi_Ye.Major(directory1)
        directory3 = ''
        m3 = HW11_XinYi_Ye.Major(directory3)
        self.assertTrue(m1.directory == directory1)
        self.assertTrue(m3.directory == directory3)
        self.assertTrue(m1.d_major == {})
        self.assertTrue(m3.d_major == {})

    def test_get_majors(self):
        """ test get_majors() method """
        directory1 = 'SIT'
        m1 = HW11_XinYi_Ye.Major(directory1)
        result1 = {'SFEN': [['SSW 540', 'SSW 555', 'SSW 810'],
                            ['CS 501', 'CS 546']], 'CS': [['CS 546', 'CS 570'], ['SSW 565', 'SSW 810']]}
        self.assertTrue(m1.get_majors() == result1)
        with self.assertRaises(ValueError):
            """ in 'CU' directory, majors file has wrong fields """
            directory2 = 'CU'
            m2 = HW11_XinYi_Ye.Major(directory2)
            m2.get_majors()
        with self.assertRaises(FileNotFoundError):
            directory3 = 'jnn'
            m3 = HW11_XinYi_Ye.Major(directory3)
            m3.get_majors()


class TestGrades(unittest.TestCase):
    """ TestStudent class: test cases in HW11_XinYi_Ye """

    def test__init(self):
        """ test __init__() method """
        directory1 = 'SIT'
        m1 = HW11_XinYi_Ye.Grade(directory1)
        directory3 = ''
        m3 = HW11_XinYi_Ye.Grade(directory3)
        self.assertTrue(m1.directory == directory1)
        self.assertTrue(m3.directory == directory3)
        self.assertTrue(m1.l_grade == [])
        self.assertTrue(m3.l_grade == [])

    def test_get_grades(self):
        """ test get_grades() method """
        directory1 = 'SIT'
        m1 = HW11_XinYi_Ye.Grade(directory1)
        result1 = [['10103', 'SSW 810', 'A-', '98763'],
                   ['10103', 'CS 501', 'B', '98762'],
                   ['10115', 'SSW 810', 'A', '98763'],
                   ['10115', 'CS 546', 'F', '98762'],
                   ['10183', 'SSW 555', 'A', '98763'],
                   ['10183', 'SSW 810', 'A', '98763'],
                   ['11714', 'SSW 810', 'B-', '98763'],
                   ['11714', 'CS 546', 'A', '98764'],
                   ['11714', 'CS 570', 'A-', '98762']]
        self.assertTrue(m1.get_grades() == result1)
        with self.assertRaises(ValueError):
            """ in 'CU' directory, grades file has wrong fields """
            directory2 = 'CU'
            m2 = HW11_XinYi_Ye.Grade(directory2)
            m2.get_grades()
        with self.assertRaises(FileNotFoundError):
            directory3 = 'jnn'
            m3 = HW11_XinYi_Ye.Grade(directory3)
            m3.get_grades()


class TestStudent(unittest.TestCase):
    """ TestStudent class: test cases in HW11_XinYi_Ye """

    def test__init(self):
        """ test __init__() method """
        directory1 = 'SIT'
        m1 = HW11_XinYi_Ye.Student(directory1)
        directory3 = ''
        m3 = HW11_XinYi_Ye.Student(directory3)
        self.assertTrue(m1.directory == directory1)
        self.assertTrue(m3.directory == directory3)
        self.assertTrue(m1.list_student == [])
        self.assertTrue(m3.list_student == [])

    def test_student_operation(self):
        """ test student_operation() method """
        with self.assertRaises(ValueError):
            """ major in students file has wrong format """
            directory2 = 'CU'
            m2 = HW11_XinYi_Ye.Student(directory2)
            m2.student_operation()
        with self.assertRaises(FileNotFoundError):
            directory3 = 'jnn'
            m3 = HW11_XinYi_Ye.Student(directory3)
            m3.student_operation()


class TestInstructor(unittest.TestCase):
    """ TestInstructor class: test cases in HW11_XinYi_Ye """

    def test__init(self):
        """ test __init__() method """
        directory1 = 'SIT'
        m1 = HW11_XinYi_Ye.Instructor(directory1)
        directory3 = ''
        m3 = HW11_XinYi_Ye.Instructor(directory3)
        self.assertTrue(m1.directory == directory1)
        self.assertTrue(m3.directory == directory3)
        self.assertTrue(m1.list_instructor == [])
        self.assertTrue(m3.list_instructor == [])

    def test_instructor_operation(self):
        """ test instructor_operation() method """
        directory1 = 'SIT'
        m1 = HW11_XinYi_Ye.Instructor(directory1)
        result = [['98764', 'Cohen, R', 'SFEN', {'CS 546': 1}], ['98763', 'Rowland, J', 'SFEN', {'SSW 810': 4, 'SSW 555': 1}], ['98762', 'Hawking, S', 'CS', {'CS 501': 1, 'CS 546': 1, 'CS 570': 1}]]
        self.assertTrue(m1.instructor_operation() == result)
        with self.assertRaises(ValueError):
            """ insturctors file in CU doesn't have header line """
            directory2 = 'CU'
            m2 = HW11_XinYi_Ye.Instructor(directory2)
            m2.instructor_operation()
        with self.assertRaises(FileNotFoundError):
            directory3 = 'jnn'
            m3 = HW11_XinYi_Ye.Instructor(directory3)
            m3.instructor_operation()


class TestRepository(unittest.TestCase):
    """ TestRepository class: test cases in HW11_XinYi_Ye """

    def test__init(self):
        """ test __init__() method """
        directory1 = 'SIT'
        m1 = HW11_XinYi_Ye.Repository(directory1)
        directory3 = ''
        m3 = HW11_XinYi_Ye.Repository(directory3)
        self.assertTrue(m1.directory == directory1)
        self.assertTrue(m3.directory == directory3)
        self.assertTrue(m1.stu == {})
        self.assertTrue(m3.stu == {})
        self.assertTrue(m1.ins == {})
        self.assertTrue(m3.ins == {})
        self.assertTrue(m1.maj == {})
        self.assertTrue(m3.maj == {})

    def test_instructor_table_db(self):
        """ test instructor_table_db() method """ 
        directory1 = 'SIT'
        m1 = HW11_XinYi_Ye.Repository(directory1)
        a, b = m1.instructor_table_db('111.db')
        result = [('98765', 'Einstein, A', 'SFEN', 'SSW 567', '4'),
                  ('98765', 'Einstein, A', 'SFEN', 'SSW 540', '3'),
                  ('98764', 'Feynman, R', 'SFEN', 'SSW 564', '3'),
                  ('98764', 'Feynman, R', 'SFEN', 'SSW 687', '3'),
                  ('98764', 'Feynman, R', 'SFEN', 'CS 501', '1'),
                  ('98764', 'Feynman, R', 'SFEN', 'CS 545', '1'),
                  ('98763', 'Newton, I', 'SFEN', 'SSW 555', '1'),
                  ('98763', 'Newton, I', 'SFEN', 'SSW 689', '1'),
                  ('98760', 'Darwin, C', 'SYEN', 'SYS 800', '1'),
                  ('98760', 'Darwin, C', 'SYEN', 'SYS 750', '1'),
                  ('98760', 'Darwin, C', 'SYEN', 'SYS 611', '2'),
                  ('98760', 'Darwin, C', 'SYEN', 'SYS 645', '1'), ]
        self.assertTrue(b == result)

    def test_repository_operation(self):
        """ test instructor_operation() method """
        with self.assertRaises(ValueError):
            directory2 = 'CU'
            m2 = HW11_XinYi_Ye.Repository(directory2)
            m2.repository_operation()
        with self.assertRaises(FileNotFoundError):
            directory4 = 'JUU'
            m4 = HW11_XinYi_Ye.Repository(directory4)
            m4.repository_operation()


if __name__ == "__main__":
    """ main function """
    unittest.main(exit=False, verbosity=2)
