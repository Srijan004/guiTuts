# ctrl+alt+n for run code

from tkinter import *

root = Tk()

def myClick() :
    myLabel = Label(root, text="Look I clicked")
    myLabel.pack()


myButton = Button(root , text="Click Me!" , command=myClick , fg="blue" ,bg="red")


myButton.pack()


root.mainloop()
