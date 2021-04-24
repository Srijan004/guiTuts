from tkinter import *
root = Tk()

myLabel1 = Label(root, text="hello world").grid(row=0,column=0)
myLabel2 = Label(root, text="my name is john walter lewis").grid(row=1,column=5) 

# myLabel1.grid(row=0,column=0)
# myLabel2.grid(row=1,column=5) 

# column=1,2,3,4 wont matter until we have something in between , so the grid system in tkinter is relative

root.mainloop()
