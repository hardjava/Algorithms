import sys
input = sys.stdin.readline

N = int(input())
inputList = list(map(int, input().split()))
inputList.sort()
currentIdx = len(inputList) - 1
count = 0
while currentIdx >= 0:
    num = inputList[currentIdx]
    endIdx = len(inputList) - 1
    startIdx = 0
    while startIdx < endIdx:
        if startIdx == currentIdx or endIdx == currentIdx:
            if startIdx == currentIdx:
                startIdx += 1
            else:
                endIdx -= 1
        else:
            sum = inputList[startIdx] + inputList[endIdx]
            if sum == num:
                count += 1
                break
            elif sum < num:
                startIdx += 1
            else:
                endIdx -= 1
    currentIdx -= 1
print(count)