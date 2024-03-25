def avg(*n):
    sum = 0
    for num in n:
        sum += num

    average = sum / len(n)
    return average


print(avg(60, 50, 40))
