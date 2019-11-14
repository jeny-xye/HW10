"""
HW08
Author: XinYi Ye
Date: 10/28/2019
"""
from datetime import datetime, timedelta
from prettytable import PrettyTable 
import os


def date_arithmetic():
    """ date_arithmetic() function: do some Date Arithmetic Operations """
    num_days = 3
    date1 = "02/27/00"
    date2 = "02/27/17"
    date3 = "10/31/17"
    date4 = "01/01/17"
    dt1 = datetime.strptime(date1, "%m/%d/%y")
    dt2 = datetime.strptime(date2, "%m/%d/%y")
    dt3 = datetime.strptime(date3, "%m/%d/%y")
    dt4 = datetime.strptime(date4, "%m/%d/%y")
    three_days_after_02272000 = (
        dt1 + timedelta(days=num_days)).strftime('%m/%d/%y')
    three_days_after_02272017 = (
        dt2 + timedelta(days=num_days)).strftime('%m/%d/%y')
    days_passed_01012017_10312017 = dt3 - dt4
    result = (three_days_after_02272000, three_days_after_02272017,
              f'{days_passed_01012017_10312017.days} days')
    return result


def file_reading_gen(path, fields, sep=',', header=False):
    """ file_reading_gen() function: field separated file reader """
    try:
        fp = open(path, 'r')
    except FileNotFoundError:    
        raise FileNotFoundError(f"can not open {path}")
    else:
        with fp:
            t = 0
            n = 0
            while True:
                try:
                    line = next(fp)
                    list = line.rstrip('\n').split(sep)
                except StopIteration:
                    break
                else:
                    if header == False:
                        t += 1
                        if len(list) == fields:
                            m = list
                            yield m
                        elif len(list) != fields:
                            raise ValueError(
                                f"This {path} has {len(list)} fields on line {t} but expected {fields} ")

                    elif header == True:
                        if n == 0:
                            if len(list) != fields:
                                raise ValueError(
                                    f"This {path} has {len(list)} fields on header but expected {fields} ")
                            else:
                                n = 1
                                continue
                        else:
                            t += 1
                            if len(list) == fields:
                                m = list
                                yield m
                            elif len(list) != fields:
                                raise ValueError(
                                    f"This {path} has {len(list)} fields on line {t} but expected {fields} ")


class FileAnalyzer:
    """ 
    FileAnalyzer class: 
    given a directory name, searches that directory for Python files and do some operations
    """

    def __init__(self, directory):
        """ a method to specify the directory which is given """
        self.directory = directory  # NOT mandatory!
        self.files_summary = dict()
        self.table = PrettyTable(
            ['Filename', 'classes', 'Fuctions', 'lines', 'characters'])

    def analyze_files(self):
        """ a method that populate the summarized data into self.files_summary """
        try:
            q = os.listdir(self.directory)
        except FileNotFoundError:
            raise FileNotFoundError('can not open this directory')
        else:
            for t in q:
                if t.endswith('.py'):
                    apath = os.path.join(self.directory, t)
                    try:
                        fp = open(apath, 'r')
                    except FileNotFoundError:
                        raise FileNotFoundError('can not open this file')
                    else:
                        with fp:
                            line_count = 0
                            ch_count = 0
                            class_count = 0
                            func_count = 0
                            for line in fp:
                                line_count += 1
                                ch_count += len(line)
                                line_new = line.lstrip(' ').rstrip(' ')
                                if line_new.startswith('class '):
                                    class_count += 1
                                elif line_new.startswith('def '):
                                    func_count += 1
                                else:
                                    continue
                            self.files_summary[t] = {
                                'class': class_count, 'function': func_count,
                                'line': line_count, 'characters': ch_count}

    def pretty_print(self):
        """ a method that print out the pretty table from the data stored in the self.files_summary """
        for key, value in self.files_summary.items():
            self.table.add_row(
                [key, value.get('class'), value.get('function'), value.get('line'), value.get('characters')])
        return self.table


if __name__ == "__main__":
    m = FileAnalyzer('810-HW06')
    m.analyze_files()
    print(m.pretty_print())
