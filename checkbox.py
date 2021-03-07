from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Learn To Code at Codemy.com")
# root.iconbitmap('c:gui/codemy.ico')
root.geometry("400x400")

def show():
	myLabel = Label(root,text=var.get()).pack()

var = StringVar()
c = Checkbutton(root,text="Would you like to SuperSize you order? Check Here!",variable=var,onvalue="SuperSize",offvalue="Burger")
c.deselect()
c.pack()


myButton = Button(root,text="Show Selection",command=show).pack()

root.mainloop()