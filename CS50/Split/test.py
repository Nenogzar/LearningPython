#
# fhand = open("softuni_pb\Lists\split.txt")
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From ') : continue
#     words = line.split()
#     print(words)
#     print(words[6])
#



spisak = open("softuni_pb\Lists\split.txt")
for line in spisak:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    # print(words)
    for index, item in enumerate(words):
        if "@" in item:
            # print(f"The first email '{item}' is at index {index}") # тествам кой е индекса
            # print(words[index])           # взимам email
            email = words[index]
            email_split = email.split("@")
            account = email_split[0]
            print(account)
