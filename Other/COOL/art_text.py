from pyfiglet import Figlet

text = "Hello SoftUni!!!"
f = Figlet(font='standard')  # Можете да изберете различни шрифтове
ascii_art = f.renderText(text)
print(ascii_art)
