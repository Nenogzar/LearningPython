number_sold_games = int(input())

hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for game in range(number_sold_games):

    game_name = input()

    if game_name == 'Hearthstone':
        hearthstone += 1

    elif game_name == 'Fornite':
        fornite += 1

    elif game_name == 'Overwatch':
        overwatch += 1

    else:
        others += 1

total_game = hearthstone + fornite + others + overwatch

print(f'Hearthstone - {hearthstone / total_game * 100:.2f}%')
print(f'Fornite - {fornite / total_game * 100:.2f}%')
print(f'Overwatch - {overwatch / total_game * 100:.2f}%')
print(f'Others - {others / total_game * 100:.2f}%')





# number_sell_games = int(input())
#
# hearthstone_sold_games = 0
# fornite_sold_games = 0
# overwatch_sold_games = 0
# other_sold_games = 0
#
# for _ in range(0, number_sell_games):
#
#     game_name = input()
#
#     if game_name == "Hearthstone":
#         hearthstone_sold_games += 1
#
#     elif game_name == "Fornite":
#         fornite_sold_games += 1
#
#     elif game_name == "Overwatch":
#         overwatch_sold_games += 1
#
#     else:
#         other_sold_games += 1
#
# hearthstone_percent_sold_games = (hearthstone_sold_games / number_sell_games) * 100
# fornite_sold_games = (fornite_sold_games / number_sell_games) * 100
# overwatch_sold_games = (overwatch_sold_games / number_sell_games) * 100
# other_sold_games = (other_sold_games / number_sell_games) * 100
#
# print(f"Hearthstone - {hearthstone_percent_sold_games:.2f}%")
# print(f"Fornite - {fornite_sold_games:.2f}%")
# print(f"Overwatch - {overwatch_sold_games:.2f}%")
# print(f"Others - {other_sold_games:.2f}%")
