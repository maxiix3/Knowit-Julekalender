def fib():
    a, b = 1, 1
    tot = 0
    while tot <= 4000000000:
        if a %2 == 0:
            tot += a
            if tot >= 4000000000:
                tot -= a
                return tot
        a, b = b, a+b
    return tot

print fib()
