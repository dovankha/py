'''
import sys

program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)

def get_full_name(first_name='Kha', last_name='Do'):
    """Print your full name from argument

    Arguments:
        first_tname: string
        last_name: string
    Returns: 
        The concat of first_name and last_name        
    """
    return f"{first_name} {last_name}"

def hello():
    a = []
    a.append(1)
    print(a)

if __name__ == '__main__':
    if count > 2:
        first_name = sys.argv[1]
        last_name = sys.argv[2]
        print(get_full_name(first_name, last_name))
    else:
        print(get_full_name())    
    hello()        


import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

try:
    if 1/1: print('Xin chao')
except:
    print('Congacon nay')   
finally:
    print('Congacon kia')         
'''

# import sys

# program_name = sys.argv[0]
# arguments = sys.argv[1:]
# count = len(arguments)

# def add(num1, num2):
#     return int(num1 + num2)

# if __name__ == '__main__':
#     try:
#         if count > 1:
#             print(add(int(sys.argv[1]), int(sys.argv[2])))
#     except:
#         print('Failed')

# --- Check file exist
# f = open("Testing.txt", 'w')
# f.write('Congacon')

# from os.path import exists

# print(exists('Testing.txt'))

# ---- create cvs files
# import csv

# header = ['STT', 'Name', 'Age']
# data = [[1, 'Kha', 20],[2, 'Trung', '21']]

# f = open("Testing.csv", 'w', encoding='UTF-8')
# writer = csv.writer(f)
# writer.writerow(header)
# writer.writerow(data)

#--- Tkinter
'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

from click import command
from sqlalchemy import true

root = tk.Tk()
root.title("N19DCAT041")
root.geometry('600x400+5+5')
root.attributes('-alpha', 0.9)  # --- set độ mờ cho window

#--- Store username & password
user_name = tk.StringVar()
passwd = tk.StringVar()

def print_hello():
    tkinter.messagebox.showinfo('Notification', 'Login succesfully!')

def show_image():
    tkinter.messagebox.showinfo('Show infor', 'Dep trai qua hehe')

def login_clicked():
    msg = f'You entered username is {user_name.get()} and password is {passwd.get()}'
    tkinter.messagebox.showinfo('Notification', msg)

message = tk.Label(root, text='Hello world').pack()
message1 = tk.Label(root, text='Xin chao').pack()

# image = tk.PhotoImage(file="D:\Coding\ThucHanhPython\976b3e7337ffc9a190ee.jpg")
# show_image_button = tk.Button(root, image=image, command=show_image).pack()
show_button = ttk.Button(root, text='Bấm dô', command=print_hello).pack()

#--- sign in frame
sigin = tk.Frame(root)
sigin.pack(padx=10, pady=10, fill='x', expand=True)

#--- username
username_label = tk.Label(sigin, text='Username')
username_label.pack(fill='x', expand=True)
username_entry = tk.Entry(sigin, textvariable=user_name).pack(fill='x', expand=True)

#--- password
passwd_label = tk.Label(sigin, text='Password')
passwd_label.pack(fill='x', expand=True)
passwd_entry = tk.Entry(sigin, textvariable=passwd, show='*').pack(fill='x', expand=True)

#--- Login button

login_button = tk.Button(sigin, text='Login', command=login_clicked).pack()

root.mainloop()
'''

#--- tkinter 2
from cgitb import text
from msilib.schema import RadioButton
import tkinter as tk
from tkinter import StringVar, ttk
from tkinter import messagebox
import tkinter

root = tk.Tk()
root.title('n19dcat041')
root.geometry('600x400+5+5')

a = StringVar()
b = StringVar()

def add():
    messagebox.showinfo('Resolve',f'{a.get()} + {b.get()} is {int(a.get()) + int(b.get())}')
    resolve_label = tk.Label(root, text=f'Resolve = {int(a.get()) + int(b.get())}').pack()

def minus(a, b):
    return int(a) - int(b)

def multiple(a, b):
    return int(a) * int(b)

def division(a, b):
    return int(a) // int(b)

a_label = tk.Label(root, text='a').pack()
a_entry = tk.Entry(root, textvariable=a).pack()
b_label = tk.Label(root, text='b').pack()
b_entry = tk.Entry(root, textvariable=b).pack()

add_button = ttk.Button(root, text='Add', command=add).pack()

# resolve_label = tk.Label(root, text=f'Resolve = {a.get() + b.get()}').pack()


root.mainloop()