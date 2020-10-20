def is_pal(num):
    num = str(num)
    if num == num[::-1]:
        return  True
    else:
        return False

if __name__ == "__main__":

    for num in range(1000,10000):
        if is_pal(num) :
            print(num)