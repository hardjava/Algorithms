N = int(input())
NList = list(map(int, input().split()))
M = int(input())
myDic = {}
MList = list(map(int, input().split()))

index = 0
for i in MList:
    myDic[i] = index
    index += 1

result = list(0 for i in range(len(myDic)))

for i in NList:
    if myDic.get(i) != None:
        result[myDic.get(i)] += 1

print(" ".join(map(str, result)))