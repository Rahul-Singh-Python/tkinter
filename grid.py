from tkinter import *

root = Tk()

# Creating at Label Widget
myLabel1 = Label(root, text="Hello Rahul")
myLabel2 = Label(root, text="Hello Akash")

# Sholving it onto the screen
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=5)

root.mainloop()