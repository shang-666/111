n = int (input())
l = list(map(int,input().strip().split()))
res = 0
for i in range(n-1):
    a = l.index(min(l))
    res += l[a]*l[a-1]*l[(a+1)%(n-i)]
    del l[a]
print(res)
