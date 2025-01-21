S, P = map(int, input().split())
inputStr = input()
condition = list(map(int, input().split()))
arr = {
    'A':0,
    'C':0,
    'G':0,
    'T':0
}

def isSatisfyCondition():
    myList = list(arr.values())
    for i in range(len(myList)):
        if myList[i] < condition[i]:
            return False
    return True

startIdx = 0
endIdx = startIdx + P - 1
count = 0

for i in inputStr[startIdx: endIdx + 1]:
    if arr.get(i) != None:
        arr[i] += 1

while True:
    if isSatisfyCondition():
        count += 1
        
    if endIdx >= len(inputStr) - 1:
        break
    
    if arr.get(inputStr[startIdx]) != None:
        arr[inputStr[startIdx]] -= 1
    if arr.get(inputStr[endIdx + 1]) != None:
        arr[inputStr[endIdx + 1]] += 1
    startIdx += 1
    endIdx += 1

print(count)