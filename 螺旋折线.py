def sum(a0, n, d):
    return (2 * a0 + (n - 1) * d) * n / 2


while 1:
    x, y = map(int, input().split())
    d = 0
    n = 0
    if (y > 0) and (abs(x) <= y):
        n = y
        d = y - x + 2 * y
    elif (x > 0) and (abs(y) <= x):
        n = x
        d = y + x
    elif (y <= 0) and (x >= y - 1) and (x <= -y):
        n = -y
        d = -(-y - x)
    elif (x < 0) and (y >= x + 1) and (y <= -x):
        n = -x - 1
        d = -(y - x - 1 - 2 * x - 1)
    print(sum(1, 2 * n, 1) * 2 - d)