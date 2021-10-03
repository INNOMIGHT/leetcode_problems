from itertools import product, repeat

def plan_the_street(n):
    ways = []
    count = 0
    for w in product(['X', 'Y'], repeat=n):
        tmp = ''.join(w)
        if "XX" not in tmp:
            ways.append(w)
            count += 1
    print(count*count)
    print(ways)

plan_the_street(3)