def create_phone_number(number):
    number = "".join(list(map(str, number)))
    return (f"({number[0:4]}) {number[4:7]}-{number[7:]}")

print(create_phone_number(input("phone number: ")))