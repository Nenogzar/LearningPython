from tkinter import *
root = Tk()
 
# създаване на обект на Менюто на главния прозорец
m = Menu(root) 
# конфигуриране на прозореца с меню
root.config(menu=m) 

# създаване на елемент на менюто
fm = Menu(m) 
m.add_cascade(label="File",menu=fm) 
fm.add_command(label="New")
fm.add_command(label="Open...") 
fm.add_command(label="Save...")
fm.add_command(label="Exit")
 
# втори елемент за менюто
hm = Menu(m) 
m.add_cascade(label="?",menu=hm)
hm.add_command(label="Help")
hm.add_command(label="About")
 
root.mainloop()
