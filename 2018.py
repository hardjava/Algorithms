N = int(input())

def getCount(N):
    i = N
    count = 0

    while i >= 1:
        sum = i
        temp = i - 1
        while sum < N:
            sum += temp
            temp -= 1
            if temp <= 0 and sum <= N:
                if sum == N:
                    return count + 1
                else:
                    return count
        if sum == N:
            count += 1
        i -= 1

    return count    

print(getCount(N))