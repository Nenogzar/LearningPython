import random

positive_even_number = random.randrange(2, 101, 2)
negative_even_number = random.randrange(-100, -1, 2)

positive_odd_number = random.randrange(1, 100, 2)
negative_odd_number = random.randrange(-101, 0, 2)
print("We now have some random numbers available for future exercises.")
print("The random positive even number is", positive_even_number)
print("The random positive odd nubmer is", positive_odd_number)
print("The random negative even number", negative_even_number)
print("The random negative odd number", negative_odd_number)



negativ_even = ""
for n in range(-100, -1, 2):
    negativ_even += str(n) + ", "

# Remove the trailing ", " from the string
negativ_even = negativ_even.rstrip(", ")

print(negativ_even)