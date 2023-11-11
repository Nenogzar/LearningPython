# Словарь заполнен по умолчанию
dict = {
    "apple" : "ябълка",
    "bold" : "мазен",
    "bus" : "автобус",
    "cat" : "котка",
    "car" : "кола"}

print("=" * 15, "Dict v 0.2", "=" * 15)

# Справочник. Извиква се с команда h
help_message = """
s - Search
a - Add new word
r - Delete the word
k - Display all words
d – Display dict
h – Help 
q - Exit
"""
    
choice = ""
while choice != "q":
    choice = input("(h - help)>> ")
    if choice == "s":
        word = input("Enter the word: ")
        res = dict.get(word, "Not Found!")
        print(res)
    elif choice == "a":
        word = input("Enter the word: ")
        value = input("Enter translation: ")
        dict[word] = value
        print("Word added!")
    elif choice == "r":
        word = input("Enter the word: ")
        del dict[word]
        print("Word deleted")
    elif choice == "k":
        print(dict.keys())
    elif choice == "d":
        for word in dict:
            print(word, ": ", dict[word])
    elif choice == "h":
        print(help_message)
    elif choice == "q":
        continue;
    else:
        print("Unrecognized command. Enter h for help")
