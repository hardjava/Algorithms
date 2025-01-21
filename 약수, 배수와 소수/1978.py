def isSosu(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

N = input()
arr = list(map(int, input().split()))
count = 0
for i in arr:
    if i != 1:
        if isSosu(i):
            count += 1
print(count)