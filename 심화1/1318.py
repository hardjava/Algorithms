def isChecker(s):
    arr = [False] * 26
    for i in range(len(s)):
        index = ord(s[i]) - ord('a')
        if arr[index] == False:
            arr[index] = True
        else:
            if s[i] != s[i - 1]:
                return 0
    return 1

a = int(input())
count = 0
for i in range(a):
    str = input()
    if isChecker(str):
        count += 1

print(count)