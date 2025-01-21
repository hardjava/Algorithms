A, B, V = map(int, input().split())

last = V - A
oneDay = A - B
value = 0
if last % oneDay != 0:
    value = last // oneDay + 2
else:
    value = last // oneDay + 1

print(value)