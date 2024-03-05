import smtplib
import os
from email.message import EmailMessage
from tkinter import messagebox

class Mail:
    address = 'iamsandeshstha@gmail.com'
    pw = 'tclv wlzi ippi yzfo'

    files=['attendance.csv']

    # contacts = ['iamsandeshstha1@gmail.com', 'aapchutiye2@gmail.com']  for multiple emails

    msg = EmailMessage()
    msg['Subject'] = "The Attendance Report"
    msg['From'] = address
    msg['To'] = 'iamsandeshstha1@outlook.com'
    # msg['To'] = ','.join(contacts) for multiple emails
    msg.set_content("The Attendance Report")

    for file in files:
        with open(file, 'rb') as f:
                file_data = f.read()
                file_name = f.name


    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(address, pw)

        smtp.send_message(msg)

