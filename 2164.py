from collections import deque

myDeque = deque(range(1, int(input()) + 1))

isPop = True
while len(myDeque) > 1:
    if isPop:
        myDeque.popleft()
    else:
        myDeque.append(myDeque.popleft())
    isPop = not isPop

print(myDeque[0])