for num in range(100, 1000):
    num_sum = pow(int(str(num)[0]), 3) + pow(int(str(num)[1]), 3) + pow(int(str(num)[2]), 3)
    if num == num_sum:
        print(num)