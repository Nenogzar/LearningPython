# Импортиране на библиотеката pywhatkit
import pywhatkit as kit

# Задаване на текста, който искате да превърнете в ръкопис
text = "hey Stoyan."

# Извикване на функцията text_to_handwriting с текста и името на изходния файл
kit.text_to_handwriting(text, "output.png")
