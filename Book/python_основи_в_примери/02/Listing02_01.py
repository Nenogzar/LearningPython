# Въвежда се число:
number=int(input("Въведете число: "))
# Докато числото е по-голямо от нула:
while number>0:
    # Последната цифра в числото:
    digit=number%10
    # Отпечатване на цифра:
    print("|"+str(digit),end="")
    # Отхвърляне на последната цифра в числото:
    number=number//10
# Показване на последния разделител:
print("|")
