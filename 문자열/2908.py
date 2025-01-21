def reverse(num):
    i = num % 10
    num = num // 10
    j = num % 10
    k = num // 10
    return i * 100 + j * 10 + k

A, B = map(int, input().split())
A = reverse(A)
B = reverse(B)

print(max(A, B))