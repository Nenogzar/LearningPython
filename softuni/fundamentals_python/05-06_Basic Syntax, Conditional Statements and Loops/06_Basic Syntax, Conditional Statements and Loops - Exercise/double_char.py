current_string = input()
while current_string != "End":
    if current_string != "SoftUni":
        new_string = ""
        for char in current_string:
            new_string += char * 2
        print(new_string)
    current_string = input()

""" 2 """

string_ = input()

while string_ != "End":
    if string_ != "SoftUni":
        [print(i * 2, end="") for i in string_]
        print()
    string_ = input()