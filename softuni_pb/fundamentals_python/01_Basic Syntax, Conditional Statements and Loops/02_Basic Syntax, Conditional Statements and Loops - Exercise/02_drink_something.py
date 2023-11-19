drinking_age = int(input())

age_info = {
    "toddy": 14,
    "coke": 18,
    "beer": 21,
    "whisky": 100
}
for drinks, age in age_info.items():
    if drinking_age <= age:
        print('drink', drinks)
        break

""" 2 """

# drinking_age = int(input())
#
# if drinking_age <= 14:
#     print("drink toddy")
#
# elif drinking_age <= 18:
#     print("drink coke")
#
# elif drinking_age <= 21:
#     print("drink beer")
#
# else:
#     print("drink whisky")

""" 3 """

# kids = "toddy"
# teen = "coke"
# young = "beer"
# adults = "whisky"
#
# age = int(input())
# if age <= 14:
#     drink = kids
# elif age <= 18:
#     drink = teen
# elif age <= 21:
#     drink = young
# elif age > 21:
#     drink = adults
# print('drink', drink)
