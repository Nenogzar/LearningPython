# You will receive a field of a tic-tac-toe game in three lines containing numbers, separated by a single space.
# Legend:
# •	0 - empty space
# •	1 - first player move
# •	2 - second player move
# Find out who the winner is. If the first player wins, print "First player won".
# If the second player wins, print "Second player won". Otherwise, print "Draw!".



lines = [input().split() for _ in range(3)]
first_player_win = None

# for player in ['1', '2']: ...`: Започва два цикъла, един за всеки играч с маркери '1' и '2'.
# Това позволява проверка за победител за всеки от двата играча.
for player in ['1', '2']:
    if (any(all(cell == player for cell in line) for line in lines)
            or any(all(line[i] == player for line in lines) for i in range(3))):
        # any(all(cell == player for cell in line) for line in lines)`:
        # Този израз проверява дали има поне един ред, в който всички елементи са равни на текущия играч ('1' или '2').
        # Функцията `any` връща `True`, ако поне един ред отговаря на условието.
        first_player_win = (player == '1')
        break

# Check diagonals for both players
for player in ['1', '2']:
    if (all(lines[i][i] == player for i in range(3))
            or all(lines[i][2 - i] == player for i in range(3))):
        # any(all(line[i] == player for line in lines) for i in range(3))`:
        # Този израз проверява дали има поне един колона, в който всички елементи са равни на текущия играч ('1' или '2')
        # Функцията `any` връща `True`, ако поне колона ред отговаря на условието.
        first_player_win = (player == '1')
        break

if first_player_win is None:
    print("Draw!")
elif first_player_win:
    print("First player won")
else:
    print("Second player won")

"""""""""
###########################################*-*FROM*CEO*-*###########################################

first_line = input().split(" ")
second_line = input().split(" ")
third_line = input().split(" ")

first_player_win = None

if len(set(first_line)) == 1 and first_line[0] == "1":
    first_player_win = True

elif len(set(second_line)) == 1 and second_line[0] == "1":
    first_player_win = True

elif len(set(third_line)) == 1 and third_line[0] == "1":
    first_player_win = True

elif first_line[0] == second_line[1] == third_line[2] and first_line[0] == "1":
    first_player_win = True

elif first_line[1] == second_line[1] == third_line[1] and first_line[1] == "1":
    first_player_win = True

elif first_line[2] == second_line[1] == third_line[0] and first_line[2] == "1":
    first_player_win = True

elif first_line[2] == second_line[2] == third_line[2] and first_line[2] == "1":
    first_player_win = True

elif first_line[0] == second_line[0] == third_line[0] and first_line[0] == "1":
    first_player_win = True

elif len(set(first_line)) == 1 and first_line[0] == "2":
    first_player_win = False

elif len(set(second_line)) == 1 and second_line[0] == "2":
    first_player_win = False

elif len(set(third_line)) == 1 and third_line[0] == "2":
    first_player_win = False

elif first_line[0] == second_line[1] == third_line[2] and first_line[0] == "2":
    first_player_win = False

elif first_line[1] == second_line[1] == third_line[1] and first_line[1] == "2":
    first_player_win = False

elif first_line[2] == second_line[1] == third_line[0] and first_line[2] == "2":
    first_player_win = False

elif first_line[2] == second_line[2] == third_line[2] and first_line[2] == "2":
    first_player_win = False

elif first_line[0] == second_line[0] == third_line[0] and first_line[0] == "2":
    first_player_win = False


if first_player_win is None:
    print("Draw!")

elif first_player_win:
    print("First player won")

else:
    print("Second player won")

"""""""""
###########################################*-*FROM*CEO*-*###########################################
"""""""""

first_row = input().split()
second_row = input().split()
third_row = input().split()

name_player = "First"
found = False

for player in range(1, 3):
    player = str(player)
    line = [player, player, player]
    if line == first_row or second_row == line or third_row == line:  # преверка на редовете
        found = True
    for index in range(0, 3):
        if first_row[index] == player and second_row[index] == player and third_row[index] == player:  # проверка на колоните
            found = True
    if first_row[0] == player and second_row[1] == player and third_row[2] == player:  # ляв диагонал
        found = True
    elif first_row[2] == player and second_row[1] == player and third_row[0] == player:  # десен диагонал
        found = True
    if found:
        print(f"{name_player} player won")
        break
    name_player = "Second"
else:
    print("Draw!")

"""""""""
