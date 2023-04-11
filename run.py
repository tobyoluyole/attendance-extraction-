
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
with open('output.txt', 'w') as f:
    for row in result:
        f.write(row[0] + '\n')
# close the database connection
cursor.close()
conn.close()

import openpyxl

# Load the Attendance excel file
wb = openpyxl.load_workbook('Attendance.xlsx')
sheet = wb.active

# Get the column index to start marking attendance
last_column = sheet.max_column
start_column = last_column + 1

# Open the output file with the names
with open('output.txt', 'r') as f:
    names = f.read().splitlines()

# Loop through the names and mark attendance in the Attendance excel file
for row in range(2, sheet.max_row + 1):
    name = sheet.cell(row=row, column=1).value
    if name in names:
        sheet.cell(row=row, column=start_column).value = True
    else:
        sheet.cell(row=row, column=start_column).value = False

# Save the Attendance excel file
wb.save('Attendance.xlsx')

'''import smtplib
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# set up email addresses and password
sender_email = 'bluetoothaddress@gmail.com'
sender_password = 'blueaddress'
receiver_email = 'tobioluyole@gmail.com','robertoszn9@gmail.com'

# set up message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = 'Attendance for today'

# add body with current date
today = date.today().strftime("%B %d, %Y")
body = f"Please find attached to this mail the attendance for {today}"
msg.attach(MIMEText(body, 'plain'))

# add attachment
filename = 'Attendance.xlsx'
with open(filename, 'rb') as f:
    attach = MIMEApplication(f.read(), _subtype="xlsx")
    attach.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(attach)

# send email
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(sender_email, sender_password)
    smtp.send_message(msg)
    print('Email sent successfully.')'''




