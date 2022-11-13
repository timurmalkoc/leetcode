def reverse(x):
    if x < -2147483648 or x > 2147483647 or -int(str(abs(x))[::-1]) < -2147483648 or int(str(abs(x))[::-1]) > 2147483647:
        return 0
    if x<0:
        return -int(str(abs(x))[::-1])    
    return int(str(abs(x))[::-1])

print(reverse(120))
print(reverse(-120))
print(reverse(221))
print(reverse(22453452432450))