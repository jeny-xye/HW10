"""
HW11
Author: XinYi Ye
Date: 11/06/2019
"""
from prettytable import PrettyTable
from collections import defaultdict
import HW08_XinYi_Ye
import os
import sqlite3


class Major:
    """ Major class: hold informations in majors.txt (major, required/elective, course) """

    def __init__(self, directory):
        """ __init__() method: two attributes directory and d_major """
        self.directory = directory
        self.d_major = defaultdict(list)

    def get_majors(self):
        """ get_majors() method: get informations in majors.txt and put them into d_major dictionary """
        path = os.path.join(self.directory, 'majors.txt')
        index_line = 1
        list = [[], []]
        sort_major = {}
        for list in HW08_XinYi_Ye.file_reading_gen(path, fields=3, sep='\t', header=True):
            index_line += 1
            l = list[2].split(' ')
            if list[0].isupper() == False:
                """ major has wrong format which should be all upper characters """
                raise ValueError(
                    f"This majors file has wrong major on line {index_line}")
            elif list[1] not in ['R', 'E']:
                """ required/elective must be 'R' or 'E' """
                raise ValueError(
                    f"This majors file has wrong Required/Elective on line {index_line}")
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
                    f"This majors file has wrong courses on line {index_line}")
            else:

                if list[0] not in self.d_major:
                    """ get d_major dictionary: {major: [[required courses], [elective courses]]}"""
                    if list[1] == 'R':
                        self.d_major[list[0]] = [[list[2]], []]
                    elif list[1] == 'E':
                        self.d_major[list[0]] = [[], [list[2]]]
                else:
                    if list[1] == 'R':
                        self.d_major[list[0]][0].append(list[2])

                    elif list[1] == 'E':
                        self.d_major[list[0]][1].append(list[2])

        for key, value in self.d_major.items():
            """ sort required course list and elective course list in d_major dictionary """
            l1 = sorted(value[0])
            l2 = sorted(value[1])
            sort_major[key] = [l1, l2]
        self.d_major = sort_major
        return self.d_major


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
        index_line = 1
        for list in HW08_XinYi_Ye.file_reading_gen(path, fields=4, sep='\t', header=True):
            index_line += 1
            l = list[1].split(' ')
            if list[0].isdigit() == False:
                """ the student cwid should be composed of numbers """
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
            elif list[2] not in ['A', 'A-', 'B', 'B+', 'B-', 'C', 'C-', 'C+', 'F']:
                """ grade should be in ['A', 'A-', 'B', 'B+', 'B-','C', 'C-', 'C+', 'F']"""
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
        index_line = 1
        stug_cwid = []
        stus_cwid = []
        stus_major = []
        stum_major = []
        g = Grade(self.directory)
        for item in g.get_grades():
            stug_cwid.append(item[0])
        m = Major(self.directory)
        copy_major = m.get_majors()
        for key in copy_major:
            stum_major.append(key)
        for list in HW08_XinYi_Ye.file_reading_gen(path, fields=3, sep='\t', header=True):
            index_line += 1
            l_completed = []
            l_required = []
            d = defaultdict(str)
            l = list[1].split(', ')
            if list[0].isdigit() == False:
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
            elif list[0] not in stug_cwid:
                """ student list[0] doesn't have grade in grades file """
                print(f"student {list[0]} is a new student without grades")
            elif list[2] not in stum_major:
                """ there is an major wich is in students file, but it is not in majors file """
                raise ValueError(f"major {list[2]} is not in majors file")
            else:

                stus_cwid.append(list[0])
                stus_major.append(list[2])
                for item in g.get_grades():
                    if item[0] == list[0]:
                        d[item[1]] = item[2]
                    else:
                        continue
                d_sort = sorted(d.items(), key=lambda d: d[0])
                l_completed = [item[0] for item in d_sort if item[1] in [
                    'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']]

                value = copy_major.get(list[2])
                l_required = [req for req in value[0]
                              if req not in l_completed]
                time = 0
                for ele in value[1]:
                    if ele in l_completed:
                        time += 1
                        break
                    else:
                        continue
                if time == 0:
                    self.list_student.append(
                        [list[0], list[1], list[2], d_sort, l_completed, l_required, value[1]])
                else:
                    self.list_student.append(
                        [list[0], list[1], list[2], d_sort, l_completed, l_required, 'None'])

        for cwid in stug_cwid:
            """ there is a student in grades file, but he is not in students file """
            if cwid not in stus_cwid:
                raise ValueError(
                    f"student {cwid} is in grades file, but it is not in students file")
            else:
                continue

        for major in stum_major:
            """ there is a major in majors file, but it doesn't exist in students file """
            if major not in stus_major:
                raise ValueError(
                    f"major {major} is in majors file, but it is not in students file")

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
        insg_cwid = []
        insi_cwid = []
        insm_major = []
        insi_major = []
        g = Grade(self.directory)
        grades_copy = g.get_grades()
        for item in grades_copy:
            insg_cwid.append(item[3])
        m = Major(self.directory)
        major_copy = m.get_majors()
        for key in major_copy:
            insm_major.append(key)
        for list in HW08_XinYi_Ye.file_reading_gen(path, fields=3, sep='\t', header=True):
            d3 = defaultdict(int)
            index_line += 1
            l = list[1].split(', ')
            if list[0].isdigit() == False:
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
            elif list[2] not in insm_major:
                """ there is a major in instructrs, but it doesn't exist in majors file """
                raise ValueError(
                    f"major {list[2]} in instructors file, but it is not in majors file")
            else:
                insi_cwid.append(list[0])
                insi_major.append(list[2])
                for item in grades_copy:
                    if item[3] == list[0]:
                        d3[item[1]] += 1
                    else:
                        continue
                self.list_instructor.append(
                    [list[0], list[1], list[2], d3])
        for cwid in insg_cwid:
            if cwid not in insi_cwid:
                raise ValueError(
                    f"instructor {cwid} is in grades file, but it is not in instructors file")
            else:
                continue
        for dept in insm_major:
            if dept not in insi_major:
                raise ValueError(
                    f"department {dept} is in majors file, but it is not in instructors file")
            else:
                continue
        return self.list_instructor


class Repository:
    """ Repository class: hold the students, instructors, grades and majors for a single University """

    def __init__(self, directory):
        """ __init__() method: four attributes directory and students dictionary, instructors dictionary and major dictionary """
        self.directory = directory
        self.maj = dict()
        self.stu = dict()
        self.ins = dict()

    def instructor_table_db(self, db_path):
        """ instructor_table_db() method:  create a new instructor PrettyTable from database """
        db = sqlite3.connect(db_path)
        l_row = []
        table = PrettyTable(
            ['InstructorCWID', 'Name', 'Dept', 'Course', 'Students'])
        query = 'select * from "Instructor summary table" '
        for row in db.execute(query):
            table.add_row(row)
            l_row.append(row)
        db.close()
        return table, l_row
        

    def repository_operation(self):
        """ repository_operation() method: store all of the data structures together in a single place """
        m = Major(self.directory)
        self.maj = m.get_majors()
        s = Student(self.directory)
        for item in s.student_operation():
            self.stu[item[0]] = item
        i = Instructor(self.directory)
        for item1 in i.instructor_operation():
            self.ins[item1[0]] = item1
        return self.maj, self.stu, self.ins

    def pretty_print(self):
        """ make tables to show the information collected """
        table1 = PrettyTable(['Dept', 'Required', 'Electives'])
        table2 = PrettyTable(['CWID', 'Name', 'Major', 'Completed Courses',
                              'Remaining Required', 'Remaining Electives'])
        table3 = PrettyTable(['CWID', 'Name', 'Dept', 'Course', 'Students'])
        maj_table = self.maj
        stu_table = self.stu
        ins_table = self.ins
        for key, value in maj_table.items():
            table1.add_row([key, value[0], value[1]])
        for value in stu_table.values():
            table2.add_row([value[0], value[1], value[2],
                            value[4], value[5], value[6]])
        for item in ins_table.values():
            for key, value in item[3].items():
                table3.add_row([item[0], item[1], item[2], key, value])
        return table1, table2, table3


if __name__ == "__main__":
    """ main function: input directory and print table  """
    directory = input('Directory name:')
    r = Repository(directory)
    try:
        r.repository_operation()
    except FileNotFoundError as e:
        print(e)
    except ValueError as m:
        print(m)
    else:
        a, b, c = r.pretty_print()
        d ,e = r.instructor_table_db('111.db')
        print(a)
        print(b)
        print(c)
        print(d)
