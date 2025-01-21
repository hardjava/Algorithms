import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N = int(input())

def isSosu(num):
    for i in range(2, int(num / 2 + 1)):
        if num % i == 0:
            return False
    return True


def DFS(num, count):
    if count >= N:
        print(num)
    else:
        for i in range(1, 10, 2):
            value = num * 10 + i
            if isSosu(value):
                DFS(value, count + 1)
        

DFS(2, 1)
DFS(3, 1)
DFS(5, 1)
DFS(7, 1)