def fib():
    a, b = 0, 1
    while a < 10000:
        a, b = b, a+b
        yield a

for i in fib():
    print('%d ' % (i))


