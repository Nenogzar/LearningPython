# Validate Credit Card Numb
# def validate(n):
#     n = list(map(int,str(n)))
#     for i in range(len(n)-1,0,-2):
#         n[i-1] = n[i-1]*2
#         if n[i-1] > 9:
#             n[i-1] = sum(list(map(int,str(n[i-1]))))
#     return sum(n)%10 == 0

# # 654456789
# credit_card = validate(654456789)
# if credit_card == True:
#     print("The card is valid")
# else:
#     print("This card is not valid")



""" 1 """


# n = 79927398713
# n = list(map(int,str(n)))
# for i in range(len(n)-1,0,-2):
#     n[i-1] = n[i-1]*2
#     print(n[i-1])
#     if n[i-1] > 9:
#         n[i-1] = sum(list(map(int,str(n[i-1]))))
# print(sum(n)%10 == 0)


""" 2 """

card_num = list(map(int, str(input('input '))))

for num in range(len(card_num)-1, 0, -2):
    card_num[num-1] = card_num[num-1]*2

    if card_num[num-1] > 9:
        card_num[num - 1] = sum(list(map(int,str(card_num[num-1]))))

if sum(card_num) % 10 == 0:
    print("Valic card")
else:
    print("Invalid card")


