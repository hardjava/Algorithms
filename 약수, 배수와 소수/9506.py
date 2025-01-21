while True:
    a = int(input())
    if a == -1:
        break

    mySet = set()
    for i in range(1, a // 2 + 1):
        if a % i == 0:
            mySet.add(i)
    mySet = sorted(mySet)
    if sum(mySet) == a:
        print(f"{a} = ", end='')
        print(" + ".join(map(str, mySet)))
    else:
        print(f'{a} is NOT perfect.')
    del mySet