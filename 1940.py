N = int(input())
M = int(input())
inputList = list(map(int, input().split()))
inputList.sort()

startIdx = 0
endIdx = len(inputList) - 1
count = 0
while startIdx < endIdx:
    sum = inputList[startIdx] + inputList[endIdx]
    if sum == M:
        count += 1
        startIdx += 1
        endIdx -= 1
    elif sum < M:
        startIdx += 1
    else:
        endIdx -= 1
        
print(count)