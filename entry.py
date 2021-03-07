from tkinter import *

root = Tk()

# e = Entry(root,width=50,bg="blue",fg="white")
# e = Entry(root,width=50,borderwidth=5)
e = Entry(root,width=50)
e.pack()
e.insert(0,"Enter Your Name : ")

def myClick():
	hello = "Hello " + e.get()
	myLabel = Label(root,text=hello)
	# myLabel = Label(root,text="Hello : "+ e.get())
	myLabel.pack()


myButton = Button(root,text="Enter Stack Quote",command=myClick)
myButton.pack()

root.mainloop()