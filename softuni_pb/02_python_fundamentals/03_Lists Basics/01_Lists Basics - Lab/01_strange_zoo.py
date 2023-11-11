head = input()
body = input()
tail = input()

text = [tail, body, head]

print(text)


################### FROM  zahariev-webbersof ####################
my_list = []

for _ in range(3):
    data = input()
    my_list.append(data)

my_list[0], my_list[2] = my_list[2], my_list[0]

print(my_list)