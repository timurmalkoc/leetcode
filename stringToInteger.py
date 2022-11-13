def myAtoi(s):
    num = ''
    flag = False
    MAX_INT = 2147483647
    MIN_INT = -2147483648
    s = s.lstrip()
    if len(s)>0 and s[0] == '-':
        s = s[1:]
        flag = True
    if len(s)>0 and s[0] == '+' and not flag:
        s = s[1:]
    for x in s:
        if x.isnumeric():
            num+=x
        else:
            break
    if num == '':
        return 0

    if flag:
        if -int(num) < MIN_INT:
            return MIN_INT
        else:
            return -int(num)
    else: 
        if int(num) > MAX_INT:
            return MAX_INT
        else:
            return int(num)

print(myAtoi("42"))
print(myAtoi("-42"))
print(myAtoi("4122 abcc"))