import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from spellchecker import SpellChecker

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.root.configure(bg="#e6e6e6")  # Set the window background color
        self.text_area = tk.Text(root, wrap="word", undo=True, bg="white")
        self.text_area.pack(expand="yes", fill="both")

        # Spellchecker
        self.corrector = SpellChecker()
        self.hint_box = tk.Listbox(root)
        self.hint_box.pack_forget()

        # Line and character count labels
        self.line_count_label = tk.Label(root, text="Lines: 0")
        self.line_count_label.pack(side="left", padx=5)
        self.char_count_per_line_label = tk.Label(root, text="Chars/Line: 0")
        self.char_count_per_line_label.pack(side="left", padx=5)
        self.total_char_count_label = tk.Label(root, text="Total Chars: 0")
        self.total_char_count_label.pack(side="left", padx=5)

        # Menu bar
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.destroy)

        # Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Select All", command=self.select_all)

        # Spellcheck menu
        self.spellcheck_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Spellcheck", menu=self.spellcheck_menu)
        self.spellcheck_menu.add_command(label="Check Word", command=self.check_word)
        self.spellcheck_menu.add_command(label="Check Word Manually", command=self.check_word_manually)

        # Bind events
        self.text_area.bind("<KeyRelease>", self.check_spelling)
        self.text_area.bind("<Key>", self.update_status)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.update_status()

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)
                self.update_status()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)
                self.update_status()

    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")
        self.update_status()

    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")
        self.update_status()

    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")
        self.update_status()

    def select_all(self):
        self.text_area.tag_add(tk.SEL, "1.0", tk.END)
        self.update_status()

    def check_word(self):
        selected_text = self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
        if selected_text:
            word = selected_text.strip()
            if word:
                if word in self.corrector:
                    messagebox.showinfo("Spellcheck Result", f"{word} is spelled correctly.")
                else:
                    correct_word = self.corrector.correction(word)
                    messagebox.showinfo("Spellcheck Result", f"Correct spelling for {word}: {correct_word}")
        else:
            messagebox.showinfo("Spellcheck Result", "Please select a word to check.")

    def check_word_manually(self):
        word = simpledialog.askstring("Spellcheck", "Enter a word to check:")
        if word:
            if word in self.corrector:
                messagebox.showinfo("Spellcheck Result", f"{word} is spelled correctly.")
            else:
                correct_word = self.corrector.correction(word)
                messagebox.showinfo("Spellcheck Result", f"Correct spelling for {word}: {correct_word}")

    def check_spelling(self, event):
        current_word = self.get_current_word()
        if current_word and not self.corrector.unknown([current_word]):
            suggestions = self.corrector.candidates(current_word)
            self.show_hint_box(suggestions)
        else:
            self.hide_hint_box()

    def get_current_word(self):
        cursor_position = self.text_area.index(tk.INSERT)
        line, column = map(int, cursor_position.split("."))
        start = f"{line}.{column-1} wordstart"
        end = f"{line}.{column} wordend"
        current_word = self.text_area.get(start, end)
        return current_word

    def show_hint_box(self, suggestions):
        self.hint_box.delete(0, tk.END)
        for suggestion in suggestions:
            self.hint_box.insert(tk.END, suggestion)
        x, y, _, _ = self.text_area.bbox(tk.INSERT)
        self.hint_box.place(x=self.root.winfo_rootx() + x, y=self.root.winfo_rooty() + y)

    def hide_hint_box(self):
        self.hint_box.place_forget()

    def update_status(self, event=None):
        lines = self.text_area.get(1.0, tk.END).split("\n")
        line_count = len(lines) - 1  # Exclude the empty line at the end
        char_count_per_line = [len(line) for line in lines]
        total_char_count = sum(char_count_per_line)

        self.line_count_label.config(text=f"Lines: {line_count}")
        #self.char_count_per_line_label.config(text=f"Chars/Line: {', '.join(map(str, char_count_per_line))}")
        self.total_char_count_label.config(text=f"Total Chars: {total_char_count}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()
