def fib(n):

    a = 0
    b = 1
    c = a+b

    for i in range(n):
        a, b, c = b, c, b+c
        print(c)


fib(100)