"""
HW09
Author: XinYi Ye
Date: 11/01/2019
"""
from prettytable import PrettyTable
from collections import defaultdict
import os


class Grade:
    """ 
    Grade class: 
    hold informations in grades.txt 
    (student CWID, course, and grade for that course, and the instructor CWID)
    """

    def __init__(self, directory):
        """ __init__() method: two attributes directory and l_grade list """
        self.directory = directory
        self.l_grade = []

    def get_grades(self):
        """ get_grades() method: get informations in grades.txt and put them into l_grade list """
        path = os.path.join(self.directory, 'grades.txt')
        index_line = 0
        try:
            fp = open(path, 'r')
        except FileNotFoundError:
            raise FileNotFoundError('can not open this grades file path')
        else:
            with fp:
                for line in fp:
                    index_line += 1
                    list = line.strip().split('\t')
                    l = list[1].split(' ')
                    if len(list) != 4:
                        """ wrong fields"""
                        raise ValueError(
                            f"This grades file has {len(list)} fields on line {index_line} but expected 4 ")
                    elif list[0].isdigit() == False:
                        """ student cwid is wrong format """
                        raise ValueError(
                            f"This grades file has wrong student cwid on line {index_line}")
                    elif len(l) != 2 or l[0].isupper() == False or l[0].isalpha() == False or l[1].isdigit() == False:
                        """ 
                        course has wrong format
                        correct format:
                        the course's name is composed of two parts
                        the first part is composed of characters
                        the first part is characters which are upper characters
                        the second part is composed of numbers
                        """
                        raise ValueError(
                            f"This grades file has wrong course on line {index_line}")
                    elif len(list[2]) not in [1, 2]:
                        """ the grade should be one or two length like A, B+"""
                        raise ValueError(
                            f"This grades file has wrong grade on line {index_line}")
                    elif list[2][0] not in ['A', 'B', 'C', 'F']:
                        """ the first part of grade should be in ['A', 'B', 'C', 'F']"""
                        raise ValueError(
                            f"This grades file has wrong grade on line {index_line}")
                    elif len(list[2]) == 2 and list[2][1] not in [' ', '+', '-']:
                        """ the second part of grades should be in [' ', '+', '-']"""
                        raise ValueError(
                            f"This grades file has wrong grade on line {index_line}")
                    elif list[3].isdigit() == False:
                        """ the teacher cwid should be composed of numbers """
                        raise ValueError(
                            f"This grades file has wrong instructor cwid on line {index_line}")
                    else:
                        self.l_grade.append(list)
                return self.l_grade


class Student:
    """ Student class: hold all informations of students.(cwid, name, major, completed courses, grades)"""

    def __init__(self, directory):
        """ __init__() method: two attributes directory and list_student """
        self.directory = directory
        self.list_student = []

    def student_operation(self):
        """ student_operation() method: collect all informations of students and put them into list_student"""
        path = os.path.join(self.directory, 'students.txt')
        index_line = 0
        try:
            fp = open(path, 'r')
        except FileNotFoundError:
            raise FileNotFoundError('can not open this students file path')
        else:
            with fp:
                m = Grade(self.directory)
                for line in fp:
                    index_line += 1
                    l_course = []
                    d = defaultdict(str)
                    list = line.strip().split('\t')
                    l = list[1].split(', ')
                    if len(list) != 3:
                        """ wrong fields"""
                        raise ValueError(
                            f"This students file has {len(list)} fields on line {index_line} but expected 3")
                    elif list[0].isdigit() == False:
                        """ student cwid has wrong format """
                        raise ValueError(
                            f"This students file has wrong cwid on line {index_line}")
                    elif ', ' not in list[1] or len(l) != 2 or l[0].isalpha() == False or l[1].isalpha() == False:
                        """ 
                        student name has wrong format
                        correct format:
                        the name is composed of two parts
                        ',' seperates two parts
                        one is first name, second is last name
                        two parts must be characters
                        the second part has only one character
                        the first characters of first and second part should be upper characters
                        """
                        raise ValueError(
                            f"This students file has wrong name on line {index_line}")
                    elif len(l[1]) != 1 or l[0][0].isupper() == False or l[1].isupper == False:
                        """ student name has wrong format """
                        raise ValueError(
                            f"This students file has wrong name on line {index_line}")
                    elif list[2].isupper() == False:
                        """ major has wrong format which should be all upper characters """
                        raise ValueError(
                            f"This students file has wrong major on line {index_line}")
                    else:
                        for item in m.get_grades():
                            if item[0] == list[0]:
                                d[item[1]] = item[2]
                                l_course.append(item[1])
                            else:
                                continue
                    l_course.sort()
                    """ sort l_course """
                    d_sort = dict()
                    for item1 in l_course:
                        d_sort[item1] = d[item1]
                    self.list_student.append(
                        [list[0], list[1], list[2], d_sort])
            return self.list_student


class Instructor:
    """ Instructor class: hold all informations of instructors.(cwid, name, department, course, students)"""

    def __init__(self, directory):
        """ __init__() method: two attributes directory and list_instructor """
        self.directory = directory
        self.list_instructor = []

    def instructor_operation(self):
        """ instructor_operation() method: collect all informations of instructors and put them into list_instructor"""
        path = os.path.join(self.directory, 'instructors.txt')
        index_line = 0
        try:
            fp = open(path, 'r')
        except FileNotFoundError:
            raise FileNotFoundError('can not open this instructors file path')
        else:
            with fp:
                m = Grade(self.directory)
                grades_copy = m.get_grades()
                for line in fp:
                    index_line += 1
                    d3 = defaultdict(int)
                    list = line.strip().split('\t')
                    l = list[1].split(', ')
                    if len(list) != 3:
                        """ wrong fields """
                        raise ValueError(
                            f"This instructors file has {len(list)} fields on line {index_line} but expected 3")
                    elif list[0].isdigit() == False:
                        """ wrong cwid format """
                        raise ValueError(
                            f"This instructors file has wrong cwid on line {index_line}")
                    elif ', ' not in list[1] or len(l) != 2 or l[0].isalpha() == False or l[1].isalpha() == False:
                        """ 
                        instructor name has wrong format
                        correct format:
                        the name is composed of two parts
                        ',' seperates two parts
                        one is first name, second is last name
                        two parts must be characters
                        the second part has only one character
                        the first characters of first and second part should be upper characters
                        """
                        raise ValueError(
                            f"This instructors file has wrong name on line {index_line}")
                    elif len(l[1]) != 1 or l[0][0].isupper() == False or l[1].isupper == False:
                        """ instructor name has wrong format """
                        raise ValueError(
                            f"This instructors file has wrong name on line {index_line}")
                    elif list[2].isupper() == False:
                        """ departmen must be all upper characters """
                        raise ValueError(
                            f"This instructors file has wrong department on line {index_line}")
                    else:
                        for item in grades_copy:
                            if item[3] == list[0]:
                                d3[item[1]] += 1
                            else:
                                continue
                    self.list_instructor.append(
                        [list[0], list[1], list[2], d3])

                return self.list_instructor


class Repository:
    """ Repository class: hold the students, instructors and grades for a single University """

    def __init__(self, directory):
        """ __init__() method: three attributes directory and students dictionary and instructors dictionary """
        self.directory = directory
        self.stu = dict()
        self.ins = dict()

    def repository_operation(self):
        """ repository_operation() method: store all of the data structures together in a single place """
        s = Student(self.directory)
        for item in s.student_operation():
            self.stu[item[0]] = item
        i = Instructor(self.directory)
        for item1 in i.instructor_operation():
            self.ins[item1[0]] = item1
        return self.stu, self.ins


if __name__ == "__main__":
    """ main function: print student_summary table and instructor_summary table in directory 'SIT' """
    directory = input('Directory name:')
    r = Repository(directory)
    stu_table, ins_table = r.repository_operation()
    table1 = PrettyTable(['CWID', 'Name', 'Completed Courses'])
    table2 = PrettyTable(['CWID', 'Name', 'Dept', 'Course', 'Students'])
    for value in stu_table.values():
        l_course = []
        for key in value[3]:
            l_course.append(key)
        table1.add_row([value[0], value[1], l_course])
    for item in ins_table.values():
        for key, value in item[3].items():
            table2.add_row([item[0], item[1], item[2], key, value])
    print(table1)
    print(table2)
