N, M = map(int, input().split())
myDict = {}
index = 0
for i in range(N):
    myDict[input()] = index
    index += 1

count = 0

for i in range(M):
    if myDict.get(input()) != None:
        count += 1

print(count)