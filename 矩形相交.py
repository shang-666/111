n = list(map(int,input().split()))
m = list(map(int,input().split()))
if n[0]>n[1]:
    n[0],n[1]=n[1],n[0]
if n[2]>n[3]:
    n[2],n[3]=n[3],n[2]
if m[0]>m[1]:
    m[0],m[1]=m[1],m[0]
if m[2]>m[3]:
    m[2],m[3]=m[3],m[2]
if min(n[2],m[2])-max(n[0],m[0])<0 or min(n[3],m[3])-max(n[1],m[1])<0:
    print("矩形不相交")
else:
    print("{:.2f}".format((max(n[0],m[0])-min(n[2],m[2]))*(max(n[1],m[1])-min(n[3],m[3]))))

