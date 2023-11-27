def find_it(seq):
    x = lambda b: seq.count(b) % 2 != 0
    return list(filter(x,seq))[0]
