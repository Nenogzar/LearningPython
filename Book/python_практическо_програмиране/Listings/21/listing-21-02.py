from tkinter import *
def b1(event):
     root.title("Left button")
def b3(event):
     root.title("Right button")
def move(event):
     root.title("Moving")
 
root = Tk()
root.minsize(width = 500, height=400)
 
root.bind('<Button-1>',b1)
root.bind('<Button-3>',b3)
root.bind('<Motion>',move)
 
root.mainloop()
