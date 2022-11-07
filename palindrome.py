def isPalindrome(x):
    return str(x) == str(x)[::-1]

print(isPalindrome(121))
print(isPalindrome(421))
print(isPalindrome(222))