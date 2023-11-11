def even_odd(number):
    result = "even" if number % 2 == 0 else "odd"
    return result

# Example usage:
num = int(input("insert number: "))
result = even_odd(num)
print(f"{num} is {result}")
