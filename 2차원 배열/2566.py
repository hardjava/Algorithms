arr = []

maxnum, maxI, maxJ = 0, 0, 0

for i in range(9):
    l = list(map(int, input().split()))
    m = max(l)
    if m > maxnum:
        maxnum = m
        maxI = i
        maxJ = l.index(m)

print(f'{maxnum}\n{maxI + 1} {maxJ + 1}')