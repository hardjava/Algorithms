N, K = map(int, input().split())
mySet = set()

for i in range(2, N // 2 + 1):
    if N % i == 0:
        mySet.add(N // i)

mySet.add(1)
mySet.add(N)
myList = list(sorted(mySet))
if K > len(myList):
    print('0')
else:
    print(myList[K - 1])