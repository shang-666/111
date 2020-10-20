n = int(input())
list = list(map(int,input().split()))
num = int(input())

for i in range(len(list)):
    if num == list[i]:
        print(i+1)
        break
else:
        print(-1)
