import pandas as pd
import sqlite3



import pandas as pd
import sqlite3

# read the excel file into a pandas DataFrame
excel_file = pd.read_excel('bluetooth_addresses.xlsx', header=None, names=['Mac_addresses'])

# connect to the database
conn = sqlite3.connect('Student_Information.db')
cursor = conn.cursor()

# retrieve the names of the students whose addresses are present in both the excel file and the database
result = cursor.execute("""
    SELECT Full_name FROM Students_details
    WHERE Mac_addresses IN (%s)
""" % ','.join(['?' for i in range(len(excel_file))]), tuple(excel_file['Mac_addresses'].tolist())).fetchall()

# print the names of the students
for row in result:
    print(row[0])

# close the database connection
cursor.close()
conn.close()

