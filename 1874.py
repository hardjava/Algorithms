def printValue():
    N = int(input())
    num = 1
    result = []
    s = []
    enterNum = []
    for i in range(N):
        enterNum.append(int(input()))
    for i in enterNum:
        while num <= i:
            s.append(num)
            result.append('+')
            num += 1
        last = s.pop()
        if last != i:
            return None
        result.append('-')
    return result

r = printValue()

if r == None:
    print('NO')
else:
    print('\n'.join(map(str, r)))