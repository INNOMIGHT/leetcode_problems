def balanced_remainders(n, arr):

    c0 = 0
    c1 = 0
    c2 = 0
    balance = n // 3
    count = 0

    for i in arr:
        print(i)
        if i % 3 == 0:
            c0 += 1
        elif i % 3 == 1:
            c1 += 1
        elif i % 3 == 2:
            c2 += 1
    print(c0, c1, c2)

    while c0 != c1 != c2 != balance:
        for num in arr:
            print(c0, c1, c2, balance)
            if c0 > balance:
                if num % 3 == 0:
                    num += 1
                    count += 1
            elif c1 > balance:
                if num % 3 == 1:
                    num += 1
                    count += 1
            elif c2 > balance:
                if num % 3 == 2:
                    num += 1
                    count += 1
    
    return count


print(balanced_remainders(6, [0, 2, 5, 5, 4, 8]))
        