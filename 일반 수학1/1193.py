X = int(input())
d = 1
num = 0
while X > num + d:
    num += d
    d += 1

count = X - num - 1
if d % 2 == 0:
    a = 1
    b = d
    for i in range(count):
        a += 1
        b -= 1
else:
    a = d
    b = 1
    for i in range(count):
        a -= 1
        b += 1

print(f'{a}/{b}')