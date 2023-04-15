import random
import smtplib
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

six_digits = random.randint(000000, 999999)
convert_string = str(six_digits)
first_three_digits, last_three_digits = convert_string[0:3], convert_string[3:]


otp = first_three_digits + '-' + last_three_digits

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'hammadgohar80@gmail.com'
smtp_password = 'gixdgsbrlcolcsja'  # This is app password.

smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
smtp_connection.ehlo()
smtp_connection.starttls()
smtp_connection.login(smtp_username, smtp_password)

def send_otp_to_email():
    to_email = email_entry.get()
    body = f'Your OTP is: {otp}'
    subject = 'Your OTP'

    from_email = smtp_username
    msg = f'Subject: {subject}\n\n{body}'
    smtp_connection.sendmail(from_email, to_email, msg)
    messagebox.showinfo(title='OTP Sent', message=f'A 6 digit OTP has been sent to {to_email}.')

def verify_otp():
    type_otp = int(otp_entry.get())
    if type_otp == six_digits:
        messagebox.showinfo(title='OTP Verification.', message='Your OTP was correct.')
        root.destroy()
    else:
        messagebox.showerror(title='OTP Verification.', message='Invalid OTP.')


root = Tk()
root.title('OTP Verification')
root.geometry('330x100')

email_label = Label(root, text='Enter Your E-mail:')
email_label.grid(row= 0, column=0, padx= 5, pady= 5)

email_entry = Entry(root, width= 30)
email_entry.grid(row=0, column=1, padx= 5, pady= 5)

otp_label = Label(root, text='Enter Your OTP:')
otp_label.grid(row=2, column=0, padx= 5, pady= 5)

otp_entry = Entry(root, width=30)
otp_entry.grid(row=2, column=1, padx= 5, pady= 5)

send_otp_button = Button(root, text='Send OTP', background='gray', command= send_otp_to_email)
send_otp_button.grid(row=3, column=0, padx= 5, pady= 5)

verify_otp_button = Button(root, text='Verify OTP', background='gray', command= verify_otp)
verify_otp_button.grid(row=3, column=1, padx= 5, pady= 5)

root.mainloop()
smtp_connection.quit()
