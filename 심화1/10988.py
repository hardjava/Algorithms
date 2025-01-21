def isPalindrome(str):
    start = 0
    end = len(str) - 1

    while start < end:
        if str[start] != str[end]:
            return 0
        start += 1
        end -= 1
    
    return 1

str = input()
print(isPalindrome(str))