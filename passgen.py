from tkinter import *
import random, string
import pyperclip


root = Tk()
root.geometry('500x250')
root.title('Password Generator')
root.resizable(0,0)

Label(root, text = 'Please complete the data:', font = 'arial 20 bold').pack()

Label(root, text = 'Password length:', font = 'arial 15').pack()
pass_leng = IntVar()
password_length = Spinbox(root, from_ = 10, to_ = 50, textvariable = pass_leng, width = 10).place(x=215,y=70)

password_letters = string.ascii_letters
password_numbers = string.digits
password_punctuation = string.punctuation
password_all = string.ascii_letters + string.digits + string.punctuation

password_string = StringVar()
def PasswordGenerator():
	password = ''
	for x in range(0,2):
		password = random.choice(password_all)
	for y in range(pass_leng.get() - 2):
		password = password + random.choice(password_all)
	password_string.set(password)

Button(root, text = 'GENERATE PASSWORD', command = PasswordGenerator).place(x=185,y=100)
Entry(root, textvariable = password_string, width = 72).place(x=32,y=150)

def PasswordCopy():
	pyperclip.copy(password_string.get())

Button(root, text = 'COPY', command=PasswordCopy).place(x=31,y=180)


root.mainloop()
