import math
magnolias = 3.25
hyacinths = 4
roses = 3.50
cacti = 8
taxrate = 0.05

number_magnolies = int(input())
number_hyacinths = int(input())
number_rosses = int(input())
number_cactus = int(input())
gift_price = float(input())

order = magnolias * number_magnolies + hyacinths * number_hyacinths + \
        roses * number_rosses + cacti * number_cactus
tax = order * taxrate

profit = order - tax
difference = abs(profit - gift_price)

if profit >= gift_price:
    print(f"She is left with {math.floor(difference)} leva.")
else:
    print(f"She will have to borrow {math.ceil(difference)} leva.")


# import math
#
# number_magnolias = int(input())
# number_hyacinths = int(input())
# number_rose = int(input())
# number_cacti = int(input())
# gift_price = float(input())
#
# magnolias_price = 3.25
# hyacinths_price = 4
# rose_price = 3.50
# cacti_price = 8
# taxes = 0.5
# total_sum = number_magnolias * magnolias_price + number_hyacinths * hyacinths_price + number_rose * rose_price + \
#             number_cacti * cacti_price
# total_sum_after_taxes = total_sum - ((total_sum * taxes) / 10)
#
# if total_sum_after_taxes < gift_price:
#     total_sum_after_taxes = gift_price - total_sum_after_taxes
#     print(f"She will have to borrow {math.ceil(total_sum_after_taxes)} leva.")
# else:
#     total_sum_after_taxes = total_sum_after_taxes - gift_price
#     print(f"She is left with {math.floor(total_sum_after_taxes)} leva.")
