a, b = map(int, input().split())
for n in range(a, b+1):
    num = n
    m = []
    while n != 1:
        for i in range(2, n+1):
            if n % i == 0:
                m.append(str(i))
                n = n//i
                break
    print("{}=".format(num), end="")
    print("*".join(m))