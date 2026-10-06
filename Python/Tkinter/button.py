from tkinter import *
from window import window

count = 0
def command():
    global count
    count+=1
    label.config(text=count)
    print(count)

def button(x):
    button = Button(text="Button", fg='black', bg='red',font=('Arial',20,'bold'))
    # button.config(image=image)
    button.config(command=command)
    # text = count
    button.pack()
label = Label(window, text=count)
label.pack()
