import sqlite3
from prettytable import PrettyTable

DB_File = 'HW11_XinYi_Ye.db'
db = sqlite3.connect(DB_File)
query = 'select * from "Instructor summary table"'
table = PrettyTable(['Instructor_CWID', 'Name', 'Dept', 'Course', 'Students'])
for row in db.execute(query):
    table.add_row(row)
print(table)