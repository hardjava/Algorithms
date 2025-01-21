T = int(input())

for i in range(T):
    step, str = input().split()
    for j in str:
        for k in range(int(step)):
            print(j, end="")
    print("")