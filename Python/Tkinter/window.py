from tkinter import *
from label import label
from button import button

window = Tk()

icon = PhotoImage(file='Tkinter/dan.png')

window.title('First GUI')
window.iconphoto(True,icon)
window.config(background="black")
window.geometry('1280x720')



button(window)
# label(window,icon)
window.mainloop()