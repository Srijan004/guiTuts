# ctrl+alt+n for run code
#this is only to check github changes
from tkinter import *

root = Tk()


e=Entry(root, width=50)
e.pack()


def myClick() :
    hello="Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root , text="Enter Your Name" , command=myClick , fg="green" ,bg="red")


myButton.pack()


root.mainloop()
