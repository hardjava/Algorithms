arr = [-1] * 26
s = input()

len = 0
for i in s:
    index = ord(i) - ord('a')
    if arr[index] == -1:
        arr[index] = len
    len += 1
    
print(" ".join(map(str, arr)))