luggage_price = float(input())
luggage_kg = float(input())
days_till_travel = int(input())
luggage_number = int(input())


additional_fee = 0

if luggage_kg < 10:
    luggage_price *= 0.20

elif luggage_kg <= 20:
    luggage_price *= 0.50


if days_till_travel < 7:
    additional_fee = 1.40
elif days_till_travel <= 30:
    additional_fee = 1.15
elif days_till_travel > 30:
    additional_fee = 1.10


total_sum = (luggage_price * additional_fee) * luggage_number
print(f'The total price of bags is: {total_sum:.2f} lv.')







# price_lagged_over_kg = float(input())
# kg_lagged = float(input())
# days_till_traveling = int(input())
# numbers_lagged = int(input())
#
# lagged_under_ten_off = 0.20
# lagged_ten_twenty_off = 0.50
# therthe_days_till_traveling = 0.10
# seventh_days_till_travel = 0.15
# under_seventh_days_till_travel = 0.40
#
# if kg_lagged < 10:
#     fees_lagged_under_kg = price_lagged_over_kg * lagged_under_ten_off
#
# elif kg_lagged >= 10 and kg_lagged <= 20:
#     fees_lagged_under_kg = price_lagged_over_kg * lagged_ten_twenty_off
#
# else:
#     fees_lagged_under_kg = price_lagged_over_kg
#
# if days_till_traveling > 30:
#     days_fees = fees_lagged_under_kg * therthe_days_till_traveling
#
# elif days_till_traveling >= 7 and days_till_traveling <= 30:
#     days_fees = fees_lagged_under_kg * seventh_days_till_travel
#
# elif days_till_traveling < 7:
#     days_fees = fees_lagged_under_kg * under_seventh_days_till_travel
#
# total_price_lagegd = "{:.2f}".format((fees_lagged_under_kg + days_fees) * numbers_lagged)
#
# print(f"The total price of bags is: {total_price_lagegd} lv. ")
#
