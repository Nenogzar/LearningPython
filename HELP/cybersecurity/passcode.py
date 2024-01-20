"""""""1 - digits"""""""

from string import digits
from itertools import product

for passcode in product(digits, repeat=4):
    print("".join(passcode))


"""""""2 - ascii_letters """""""

# from string import ascii_letters
# from itertools import product
#
# for passcode in product(ascii_letters, repeat=4):
#     print("".join(passcode))

"""""""3 - ascii_letters, digits, punctuation """""""

# from string import ascii_letters, digits, punctuation
# from itertools import product
#
# for passcode in product(ascii_letters + digits + punctuation, repeat=4):
#     print("".join(passcode))
