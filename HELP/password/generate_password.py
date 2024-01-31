import random
import string


def generate_password(length):
    # define the character pool fir the password generator
    characters = string.ascii_letters + string.digits + string.punctuation

    # generate a password by rndomly selection sharacters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))

    # Return the generated password
    return password


password_length = int(input("Enter the desired lenght of the password: "))

# Generatthe password usin the specified length
generated_password = generate_password(password_length)

# print the generated password
print("generated Password: ", generated_password)
