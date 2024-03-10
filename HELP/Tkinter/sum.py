import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.first_num_entri = tk.Entry()
        self.plus_sign = tk.Label(text="+")
        self.second_num_entri = tk.Entry()
        self.equal_sign = tk.Label(text="=")
        self.result_label = tk.Label(text="Result....", bg="green", fg="white")
        self.calc_buton = tk.Button(text="Calculate", command=self.calculate)

        # place widgets
        self.first_num_entri.pack(side="left")
        self.plus_sign.pack(side="left")
        self.second_num_entri.pack(side="left")
        self.equal_sign.pack(side="left")
        self.result_label.pack(side="left")
        self.calc_buton.pack(side="left")

    def calculate(self):
        first_value = float(self.first_num_entri.get())
        second_value = float(self.second_num_entri.get())
        result = first_value + second_value
        self.result_label.config(text=str(result), bg="green", fg="white")

# create the application
app = Application()
app.master.title("Result")
app.master.minsize(width=100, height=50)

# start program
app.mainloop()
