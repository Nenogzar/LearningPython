def output(event):
     # Получаваме съдържанието на текстовото поле
     s = ent.get()
     try:
        txt = open(s, "r", encoding='utf-8')
        content = txt.read()
        tex.delete(1.0,END)
        tex.insert(END, content)
     except:
        tex.delete(1.0,END)
        tex.insert(END, "File not exists")

         
from tkinter import *
root = Tk()

# Създаваме уиджети
ent = Entry(root,width=20)
but = Button(root,text="Open")
tex = Text(root,width=80,height=30,font="Courier 12",wrap=WORD)
tex.insert(END, "Enter filename and press Open")

# Разполагаме уиджетите в прозореца на програмата
ent.grid(row=0,column=0)
but.grid(row=2,column=0)
tex.grid(row=1,column=0)

# Задаваме обработчик на събития
but.bind("<Button-1>",output)

# Стартираме програмата
root.mainloop()
