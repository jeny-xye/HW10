"""
HW12
Author: XinYi Ye
Date: 11/19/2019
"""

from flask import Flask, render_template
import sqlite3

app = Flask(__name__, template_folder='templates')

@app.route('/instructors')
def show_instructor():
    """ show_instructor() function: display instructor_summary table using data from database """
    try:
        db = sqlite3.connect('111.db')
    except sqlite3.OperationalError:
        return f"can't open this database"
    else:
        query = """select i.CWID, i.Name, i.Dept, g.Course, Count(g.Course) as Students 
                from instructors i join grades g on i.CWID = g. InstructorCWID 
                group by i.CWID, i.Name, g.Course"""

        rows = [{'CWID': CWID, 'Name': Name, 'Dept': Dept, 'Course': Course, 'Students': Students}
                for CWID, Name, Dept, Course, Students in db.execute(query)]
        db.close()

        return render_template('instructor_summary.html',
                               title='Stevens Repository',
                               table_title='Courses and student counts',
                               rows=rows)

app.run(debug=True)
