from tkinter import *
 
def exit_(event):
     root.destroy()
def caption(event):
     t = ent.get()
     lbl.configure(text = t)
 
root = Tk()

# Създаваме уиджети 
ent = Entry(root, width = 40)
lbl = Label(root, width = 80)

# Разполагаме уиджетите
ent.pack()
lbl.pack()
 
ent.bind('<Return>',caption)
root.bind('<Control-z>',exit_)
 
root.mainloop()
