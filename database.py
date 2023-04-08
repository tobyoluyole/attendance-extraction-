# creating the table and columns 
'''import sqlite3


conn = sqlite3.connect("Student_Detials.db")

# creating a cursor object 
cursor = conn.cursor()
# create table
cursor.execute('''
    #CREATE TABLE Students_details
    #(Full_names TEXT, Matric_number INTEGER, Mac_addresses TEXT)
''')

# commit changes and close connection
conn.commit()
conn.close()'''


'''# inserting Names into the Full_names column 
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("Student_Detials.db")

# Create a cursor object
cursor = conn.cursor()

# Insert data into table
names = ['Abdulahi Abubakar', 'Abimbola Adeyemi', 'Adaku Nwachukwu', 'Adedayo Folarin', 'Chibuzo Okoli', 'Chinwe Uzoma', 'Emeka Okafor', 'Funmilayo Akindele', 'Ibrahim Suleiman', 'Ifeoma Eze', 'Jamila Mohammed', 'Kehinde Alade', 'Lola Ogunleye', 'Mabel Okonkwo', 'Nneka Okafor', 'Obinna Nwosu', 'Olumide Adeleke', 'Oluwafunmilayo Balogun', 'Tosin Olatunji', 'Uchechi Nwafor']
for name in names:
    cursor.execute("INSERT INTO Students_details (Full_names) VALUES (?)", (name,))

# Commit changes and close connection
conn.commit()
conn.close()'''

# INSERTING MATRIC NO 
'''import sqlite3

# Connect to the database
conn = sqlite3.connect("Student_Detials.db")

# Create a cursor object
c = conn.cursor()

# Insert data into the table
matric_numbers = ["12/ENG02/001", "12/ENG02/002", "12/ENG02/003", "12/ENG02/004", "12/ENG02/005", "12/ENG02/006", 
                  "12/ENG02/007", "12/ENG02/008", "12/ENG02/009", "12/ENG02/010", "12/ENG02/011", "12/ENG02/012", 
                  "12/ENG02/013", "12/ENG02/014", "12/ENG02/015", "12/ENG02/016", "12/ENG02/017", "12/ENG02/018", 
                  "12/ENG02/019", "12/ENG02/020"]
for matric_number in matric_numbers:
    c.execute("INSERT INTO Students_details (Matric_number) VALUES (?)", (matric_number,))

# Save changes to the database
conn.commit()

# Close the database connection
conn.close()'''

import sqlite3

# Connect to the database
conn = sqlite3.connect("Student_Detials.db")
# Create a cursor object to execute SQL statements
c = conn.cursor()

# Define the list of Bluetooth Mac addresses
'''mac_addresses = ['10:1F:2E:8A:45:7C', 'E3:7C:3D:F9:1A:5B', '5F:AF:56:EA:77:08', '43:8B:9F:CE:6A:DD',
                 '6D:FA:F2:4B:60:12', 'C4:4B:4D:EB:AA:25', '51:BA:E1:11:1E:2C', '9C:48:99:53:40:19',
                 '32:47:6B:16:17:2A', 'F9:11:EC:92:B4:7D', '24:2B:4C:AF:F1:60', '4F:CC:CD:75:80:8B',
                 'A7:72:08:62:C7:89', '83:F2:1E:34:60:12', 'C5:0F:C3:DE:E7:25', '1B:8E:1C:70:BD:48',
                 'D8:69:35:C9:F1:3E', 'AC:12:03:57:66:55', '1C:52:16:A7:93:94', 'AC:23:34:28:DF:42']

# Define the SQL statement to insert the Mac addresses into the table
insert_query = "INSERT INTO Students_details (Mac_addresses) VALUES (?)"

# Execute the SQL statement for each Mac address in the list
for address in mac_addresses:
    c.execute(insert_query, (address,))

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()'''


import sqlite3

# Create a connection to the database
'''conn = sqlite3.connect('Student_Information.db')

# Create a cursor object to execute SQL statements
c = conn.cursor()

# Create the Students_details table with Full_name, Matric_no, and Mac_addresses columns
c.execute('''
          #CREATE TABLE Students_details
          #(Full_name TEXT,
           #Matric_no TEXT,
           #Mac_addresses TEXT)
          #''')

# Commit the changes to the database
#conn.commit()

# Close the database connection
#conn.close()'''


import sqlite3

# create connection to database
conn = sqlite3.connect('Student_Information.db')

# create cursor object
c = conn.cursor()

# create table
c.execute('''CREATE TABLE Students_details
             (Full_name text, Matric_no text, Mac_addresses text)''')

# insert data into table
students_data = [
    ('Abdulahi Abubakar', '12/ENG02/001', '10:1F:2E:8A:45:7C'),
    ('Abimbola Adeyemi', '12/ENG02/002', 'E3:7C:3D:F9:1A:5B'),
    ('Adaku Nwachukwu', '12/ENG02/003', '5F:AF:56:EA:77:08'),
    ('Adedayo Folarin', '12/ENG02/004', '43:8B:9F:CE:6A:DD'),
    ('Chibuzo Okoli', '12/ENG02/005', '6D:FA:F2:4B:60:12'),
    ('Chinwe Uzoma', '12/ENG02/006', 'C4:4B:4D:EB:AA:25'),
    ('Emeka Okafor', '12/ENG02/007', '51:BA:E1:11:1E:2C'),
    ('Funmilayo Akindele', '12/ENG02/008', '9C:48:99:53:40:19'),
    ('Ibrahim Suleiman', '12/ENG02/009', '32:47:6B:16:17:2A'),
    ('Ifeoma Eze', '12/ENG02/010', 'F9:11:EC:92:B4:7D'),
    ('Jamila Mohammed', '12/ENG02/011', '24:2B:4C:AF:F1:60'),
    ('Kehinde Alade', '12/ENG02/012', '4F:CC:CD:75:80:8B'),
    ('Lola Ogunleye', '12/ENG02/013', 'A7:72:08:62:C7:89'),
    ('Mabel Okonkwo', '12/ENG02/014', '83:F2:1E:34:60:12'),
    ('Nneka Okafor', '12/ENG02/015', 'C5:0F:C3:DE:E7:25'),
    ('Obinna Nwosu', '12/ENG02/016', '1B:8E:1C:70:BD:48'),
    ('Olumide Adeleke', '12/ENG02/017', 'D8:69:35:C9:F1:3E'),
    ('Oluwafunmilayo Balogun', '12/ENG02/018', 'AC:12:03:57:66:55'),
    ('Tosin Olatunji', '12/ENG02/019', '1C:52:16:A7:93:94'),
    ('Uchechi Nwafor', '12/ENG02/020', 'AC:23:34:28:DF:42')
]

c.executemany("INSERT INTO Students_details VALUES (?, ?, ?)", students_data)

# commit changes and close connection
conn.commit()
conn.close()


