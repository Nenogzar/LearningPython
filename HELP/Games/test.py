alph = 'ABCX'
answ = 0
for a in alph:
    for b in alph:
        for c in alph:
            for d in alph:
                for e in alph:
                    if a == 'X' and b != 'X' and c != 'X' and d != 'X' and e != 'X':
                        answ += 1
                    if a != 'X' and b == 'X' and c != 'X' and d != 'X' and e != 'X':
                        answ += 1
                    if a != 'X' and b != 'X' and c == 'X' and d != 'X' and e != 'X':
                        answ += 1
                    if a != 'X' and b != 'X' and c != 'X' and d == 'X' and e != 'X':
                        answ += 1
                    if a != 'X' and b != 'X' and c != 'X' and d != 'X' and e == 'X':
                        answ += 1
print(answ)