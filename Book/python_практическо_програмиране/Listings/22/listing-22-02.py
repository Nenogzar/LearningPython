from tkinter import *
 
root = Tk()
 
var0=StringVar() # стойността на всеки превключвател 
var1=StringVar() # се пази в собствена променлива
var2=StringVar()
# ако е поставена отметка, в асоциираната променлива 
# (var0,var1 или var2) се присвоява стойността onvalue, 
# ако съответно няма отметка - offvalue.
ch0 = Checkbutton(root,text="Windows",variable=var0,
          onvalue="windows",offvalue="-")
ch1 = Checkbutton(root,text="Linux",variable=var1,
          onvalue="linux",offvalue="-")
ch2 = Checkbutton(root,text="macOS",variable=var2,
          onvalue="macos",offvalue="-")
 
lis = Listbox(root,height=3)
def result(event):
     v0 = var0.get()
     v1 = var1.get()
     v2 = var2.get()
     l = [v0,v1,v2]    # стойностите на променливите се поставят в списък
     lis.delete(0,2)   # предходното съдържание се изтрива от Listbox
     for v in l:       # съдържанието на списък l е последователно...
          lis.insert(END,v) # ...поставя се в Listbox
 
but = Button(root,text="Get values")
but.bind('<Button-1>',result)
 
ch0.deselect()      # „по подразбиране” отметките не са поставени
ch1.deselect()
ch2.deselect()
 
ch0.pack()
ch1.pack()
ch2.pack()
but.pack()
lis.pack()
 
root.mainloop()
