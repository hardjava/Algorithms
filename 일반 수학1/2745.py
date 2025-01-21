def getNum(str):
    if ord(str) >= ord('A') and ord(str) <= ord('Z'):
        temp = ord(str) - ord('A')
        value = 10 + temp
        return value
    else:
        return int(str)

N, M = map(str, input().split())
M = int(M)
place = 0
length = len(N) - 1
sum = 0
while length >= 0:
    num = getNum(N[length])
    sum = sum + num * pow(M, place)
    place += 1
    length -= 1

print(sum)