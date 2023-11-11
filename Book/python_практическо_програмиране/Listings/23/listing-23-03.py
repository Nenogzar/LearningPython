from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import fileinput
 
def _open():
     op = askopenfilename()
     print(op)
     f = open(op, "r", encoding='utf-8')
     content = f.read()
     txt.delete(1.0,END)
     txt.insert(END, content)

def _save():
     sa = asksaveasfilename()
     content = txt.get(1.0,END)
     f = open(sa,"w", encoding='utf-8')
     f.write(content)
     f.close()

def close_win():
     if askyesno("Exit", "Are you sure?"):
          root.destroy()
 
def about():
     showinfo("Editor", "The simple text editor")     

 
root = Tk()
 
m = Menu(root)
root.config(menu=m)
 
fm = Menu(m)
m.add_cascade(label="File",menu=fm)
fm.add_command(label="Open...",command=_open)
fm.add_command(label="Save as...",command=_save)
fm.add_command(label="Exit",command=close_win)

hm = Menu(m)
m.add_cascade(label="Help",menu=hm)
hm.add_command(label="About",command=about)
 
txt = Text(root,width=40,height=15,font="Courier 10")
txt.pack()
 
root.mainloop()
