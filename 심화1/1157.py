str = input()
str = str.upper()

arr = list(0 for i in range(26))

for i in str:
    arr[ord(i) - ord('A')] += 1 

maximum = max(arr)

if arr.count(maximum) != 1:
    print('?')
else:
    print(chr(arr.index(maximum) + ord('A')))