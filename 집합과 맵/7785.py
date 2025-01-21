N = int(input())
myDic = {}
for i in range(N):
    name, status = input().split()
    if status == 'enter':
        myDic[name] = 'enter'
    elif status == 'leave':
        if myDic.get(name) != None:
            myDic.pop(name)

myList = [*myDic.keys()]
myList.sort()
myList.reverse()

for i in myList:
    print(i)