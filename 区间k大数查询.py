n = int(input())
li = list(map(int,input().split()))
m = int(input())
a=[]
for i in range(m):
    a.append(list(map(int,input().split())))
for j in a:
    l = int(j[0])-1
    print("l的值是",l)
    r = int(j[1])
    k = int(j[2])
    l1 = sorted(li[l:r],reverse=True)
    print(l1[k-1])
