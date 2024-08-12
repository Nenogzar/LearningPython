"""""""""
a = 0
b = 1
n = int(input("Кое по ред число на Фибоначи искате да изведа? "))

if n <= 0:
    print("Моля, въведете положително цяло число")
else:
    for i in range(n):
        c = a + b
        a = b
        b = c
    print(a)
"""""""""
l, m = 0, 1     # начални стойности на реда
upper_limit = int(input("Въведете горната граница на редицата на Фибоначи: "))

fibonacci_sequence_l = []    # Дефинира списъка съхраняващ стойностите
fibonacci_sequence_m = []
fibonacci_sequence =[]
fibonacci_sequence_nested = []
while l < upper_limit:
    fibonacci_sequence_l.append(l)
    fibonacci_sequence_m.append(m)
    l, m = m, l + m
    fibonacci_sequence = fibonacci_sequence_l + fibonacci_sequence_m    # +
    fibonacci_sequence_nested = [fibonacci_sequence_l, fibonacci_sequence_m]    # nested lists

# Използвайте join, за да обедините елементите в низ със запетаи и изпечатайте го
print(', '.join(map(str, fibonacci_sequence_l)))
print(', '.join(map(str, fibonacci_sequence_m)))
print(', '.join(map(str, fibonacci_sequence)))
print(', '.join(map(str, fibonacci_sequence_nested)))