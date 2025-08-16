def numberReverseOrder(i, n):
    if i > n:
        return
    numberReverseOrder(i+1, n)
    print(i, end= " ")


numberReverseOrder(1,5) # 5 4 3 2 1

