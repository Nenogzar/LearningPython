from functools import lru_cache


def moves(h):
    x = h[0]
    y = h[1]
    return (x, y * 2), (x * 2, y), (x, y + 1), (x + 1, y)


@lru_cache(None)
def game(h):
    if sum(h) >= 100:
        return 'WIN'
    elif any(game(m) == 'WIN' for m in moves(h)):
        return 'P1'
    elif all(game(m) in ['P1'] for m in moves(h)):
        return 'V1'
    elif any(game(m) == 'V1' for m in moves(h)):
        return 'P2'
    elif all(game(m) in ['P1', 'P2'] for m in moves(h)):
        return 'V2'


def p19(h):
    return any(game(m) == 'P1' for m in moves(h))


print([s for s in range(1, 100) if p19((s, 20))]) #Стоян играе първи ход
print([s for s in range(1, 100) if game((s, 20)) == 'P2']) #Биляна играе втори ход
print([s for s in range(1, 100) if game((s, 20)) == 'V2'])


