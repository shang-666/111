list = []
for i in range(4):
    list.append(i)
for j in range(4,1000):
    list.append(list[j-1]+list[j-3])
while True:
    n = int(input())
    if n==0:
        break
    print(list[n])