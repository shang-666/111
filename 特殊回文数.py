def is_pal(num):
    num = str(num)
    if num == num[::-1]:
        return True
    else :
        False
def sun_num(num):
    sum = 0
    num = str(num)
    for i in range(len(num)):
        sum += int(num[i])
    return sum
if __name__ == '__main__':
    n = int(input())
    for num in range(10000,1000000):
        if is_pal(num) and sun_num(num) == n:
            print(num)

