from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Images")
# root.iconbitmap('tkinter/codemy.ico')

my_img1 = ImageTk.PhotoImage(Image.open("images/2.jpeg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/1.JPG"))
my_img3 = ImageTk.PhotoImage(Image.open("images/3.JPG"))
my_img4 = ImageTk.PhotoImage(Image.open("images/4.JPG"))
my_img5 = ImageTk.PhotoImage(Image.open("images/5.JPG"))
my_img6 = ImageTk.PhotoImage(Image.open("images/6.JPG"))
my_img7 = ImageTk.PhotoImage(Image.open("images/7.JPG"))

my_label = Label(image=my_img)
my_label.pack()










button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()