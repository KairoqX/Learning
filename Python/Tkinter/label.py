from tkinter import *

def label(a, icon):
    label = Label(a,text="Dantalian", font=("Arial",50,"bold"))
    label.config(bg='black',fg='red',image=icon,padx=20,pady=20,compound=TOP )
    label.pack()