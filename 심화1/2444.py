N = int(input())
star = 1
blank = N - star

for i in range(N * 2 - 1):
    print(' ' * blank, end='')
    print('*' * star)
    if i < N - 1:
        star += 2
        blank -= 1
    else:
        star -= 2
        blank += 1