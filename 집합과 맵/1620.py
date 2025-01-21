M, N = map(int, input().split())
myDict = {}
index = 0
for i in range(M):
    myDict[input()] = index
    index += 1

for i in range(N):
    if str(i).isdigit():
        print(myDict.fromkeys(str(i)))
    else:
        print(myDict.get(i))
