M = int(input())
N = int(input())
arr = [False] * (N + 1)

for i in range(2, N // 2 + 1):
    num = i * 2
    while num <= N:
        arr[num] = True
        num += i
result = []

for i in range(M, N + 1):
    if arr[i] == False:
        result.append(i)

if result.count(1) != 0:
    result.remove(1)
    
if len(result) == 0:
    print('-1')
else:
    print(sum(result))
    print(result[0])