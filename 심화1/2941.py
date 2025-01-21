arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
str = input()
count = 0
for i in arr:
    if str.find(i) != -1:
        count += str.count(i)
        str = str.replace(i, ' ')

str = str.replace(' ', '')
count += len(str)

print(count)