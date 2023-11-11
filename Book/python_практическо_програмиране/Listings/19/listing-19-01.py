from tkinter import *
 
def hello(event):
     print ("Hello World!")
 
root = Tk()
but1 = Button(root)
but1["text"] = "Hello"
but1.bind("<Button-1>",hello)
 
but1.pack()
root.mainloop()
