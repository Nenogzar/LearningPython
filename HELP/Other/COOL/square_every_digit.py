def square_digits(num):
    return(int("".join(list(map(lambda x: str(int(x)*int(x)) ,(str(num)))))))

print(square_digits(int(input("Input number"))))