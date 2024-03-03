# Четене на въведения текст
input_text = input("Въведете текст: ")

# Разделяне на текста на нов ред при срещане на символа %
lines = input_text.split("%")

# Записване на резултата във файл
with open("output.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")

print("Резултатът е записан в output.txt")
