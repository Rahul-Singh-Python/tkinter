from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("Learn To Code at Codemy.com")
# root.iconbitmap('c:gui/codemy.ico')

def open():
	global my_img
	top = Toplevel()
	root.title("My Second Window")
	my_img = ImageTk.PhotoImage(Image.open("images/2.jpeg"))
	my_label = Label(top,image=my_img).pack()
	btn2 = Button(top,text="Close Window",command=top.destroy).pack()

btn = Button(root,text="Open Second Window",command=open).pack()


mainloop()