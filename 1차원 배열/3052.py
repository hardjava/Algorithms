s1 = set()

for i in range(10):
    num = int(input()) % 42
    s1.add(num)

print(len(s1))