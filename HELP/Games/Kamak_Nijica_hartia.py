import random

total_games = 0
total_repeats = 0
player_wins = 0
computer_wins = 0
equal = 0

while True:
    total_games += 1
    total_repeats += 1

    # Get user choice
    while True:
        user_choice = input("Изберете: камък, ножица, или хартия: ").lower()
        if user_choice == "камък" or user_choice == "ножица" or user_choice == "хартия":
            break
        else:
            print("Невалиден избор. Моля, опитайте отново.")

    computer_choice = random.choice(["камък", "ножица", "хартия"])

    print(f"Играчът избра: {user_choice}")
    print(f"Компютърът избра: {computer_choice}")

    if user_choice == computer_choice:
        winner = "Равенство"
    elif (user_choice == "камък" and computer_choice == "ножица") or \
         (user_choice == "ножица" and computer_choice == "хартия") or \
         (user_choice == "хартия" and computer_choice == "камък"):
        winner = "играч"
    else:
        winner = "компютър"

    if winner == "играч":
        player_wins += 1
        print(f"Играча печели!")
    elif winner == "компютър":
        computer_wins += 1
        print(f"Компютъра печели!")
    else:
        print(f"Равенство!")
        equal += 1

    print(f"Резултат - Играч: {player_wins}, Компютър: {computer_wins}, "
          f"\nРавенства: {equal} от общо {total_games} игри")

    play_again_choice = input("Искате ли да играете отново (да/не)? ").lower()
    if play_again_choice != "да":
        print("Благодаря за играта!")
        break

####
#####
######
# import random
#
# total_games = 0
# total_repeats = 0
# player_wins = 0
# computer_wins = 0
# equal = 0
#
# while True:
#     total_games += 1
#     total_repeats += 1
#
#     # Get user choice
#     while True:
#         user_choice = input("Изберете: камък, ножица, или хартия: ").lower()
#         if user_choice in ["камък", "ножица", "хартия"]:
#             break
#         else:
#             print("Невалиден избор. Моля, опитайте отново.")
#
#     computer_choice = random.choice(["камък", "ножица", "хартия"])
#
#     print(f"Играчът избра: {user_choice}")
#     print(f"Компютърът избра: {computer_choice}")
#
#     if (user_choice == computer_choice):
#         winner = "Равенство"
#     elif (user_choice == "камък" and computer_choice == "ножица") or \
#          (user_choice == "ножица" and computer_choice == "хартия") or \
#          (user_choice == "хартия" and computer_choice == "камък"):
#         winner = "играч"
#     else:
#         winner = "компютър"
#
#     if winner == "играч":
#         player_wins += 1
#         print(f"Играча печели!")
#     elif winner == "компютър":
#         computer_wins += 1
#         print(f"Компютъра печели!")
#     else:
#         print(f"Равенство!")
#         equal += 1
#
#     print(f"Резултат - Играч: {player_wins}, Компютър: {computer_wins}, "
#           f"\nРавенства: {equal} от общо {total_games} игри")
#
#     play_again_choice = input("Искате ли да играете отново (да/не)? ").lower()
#     if play_again_choice != "да":
#         print("Благодаря за играта!")
#         break



################################
##############################
# import random
#
# # дефинира функция която присвоява избора на играча
# def get_user_choice():
#     while True:
#         user_choice = input("Изберете: камък, ножица, или хартия: ").lower()
#         if user_choice in ["камък", "ножица", "хартия"]:
#             return user_choice
#         else:
#             print("Невалиден избор. Моля, опитайте отново.")
#
# # Функция с условията на играта
# def determine_winner(player_choice, computer_choice):
#     if player_choice == computer_choice:
#         return "Равенство"
#     elif (player_choice == "камък" and computer_choice == "ножица") or \
#             (player_choice == "ножица" and computer_choice == "хартия") or \
#             (player_choice == "хартия" and computer_choice == "камък"):
#         return "играч"
#     else:
#         return "компютър"
#
# #функция за повторение на играта
# def play_again():
#     return input("Искате ли да играете отново (да/не)? ").lower() == "да"
#
# total_games = 0
# total_repeats = 0
# player_wins = 0
# computer_wins = 0
# equal = 0
#
# # броячи на повторенията на играта
# while True:
#     total_games += 1
#     total_repeats += 1
#     user_choice = get_user_choice()
#     computer_choice = random.choice(["камък", "ножица", "хартия"])
#
#     print(f"Играчът избра: {user_choice}")
#     print(f"Компютърът избра: {computer_choice}")
#
#     winner = determine_winner(user_choice, computer_choice)
#
#
# # броячи на резултатите
#     if winner == "играч":
#         player_wins += 1
#         print(f"Играча печели!")
#     elif winner == "компютър":
#         computer_wins += 1
#         print(f"Компютъра печели!")
#     else:
#         print(f"Равенство!")
#         equal += 1
#
#     print(f"Резултат - Играч: {player_wins}, Компютър: {computer_wins}, "
#           f"\nРавенства: {equal} от общо {total_games} игри")
#
#     if not play_again():
#         print("Благодаря за играта!")
#         break
