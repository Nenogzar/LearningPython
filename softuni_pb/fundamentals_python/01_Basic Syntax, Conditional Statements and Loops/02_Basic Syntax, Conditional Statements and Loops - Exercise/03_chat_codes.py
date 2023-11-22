chat_num = int(input())
message = ""
for _ in range(chat_num):
    message_num = int(input())

    if message_num == 88:
        message = "Hello"
    elif message_num == 86:
        message = "How are you?"
    elif message_num < 88:
        message = "GREAT!"
    else: # elif message_num > 88:
        message = "Bye."
    print(message)
