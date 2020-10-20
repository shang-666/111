'''n = int(input())
nums = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if j == 0:
            nums[i][j] = 1
        else:
            nums[i][j] = nums[i - 1][j - 1] + nums[i - 1][j]

for i in range(n):

    for j in range(n):
        if nums[i][j] != 0:
            print(nums[i][j], end=" ")
    print()
'''
n = int(input())
N = [1]
for m in range(n):  #打印10行
    for i in range(len(N)):
        if i == len(N) - 1:
            print(N[i])
        else:
            print(N[i],end=' ')
    N.append(0)
    N = [N[k] + N[k-1] for k in range(i+2)]