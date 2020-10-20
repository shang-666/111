k = eval(input()) #输入一个数给k，用k来控制有多少个DNA

for kk in range(k):
    m,n = map(int,input().split()) #m表示每一行有多少个符号，n表示有多少个DNA链
    p = 0  #用p来控制x的位置
    for i in range(m*n-n+1):    #循环控制行数及每行输出
        l = list(" "*m)         #初始化列表为m个空格
        if p == i%(m-1):        #当p的值与i%(m-1)相同时，则将列表中位置p和m-1-p的值改为'X'
            l[p] = 'X'
            l[m-p-1] = 'x'
        for s in l:             #将修改过的列表在一行中输出
            print(s,end='')
        p += 1                  #将p的值加1，以对应下一行x的位置
        print()                 #控制换行
        if p == m-1:            #当p == m-1 时，又回到为0时的输出位置
            p = 0
    print()


