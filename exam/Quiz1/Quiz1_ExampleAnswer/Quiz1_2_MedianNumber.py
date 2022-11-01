a, b, c = eval(input("Input three number: "))  # 以eval轉換成數值值及使用多重指定(a,b,c)

if a > b:  # if...elif..else條件判斷
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c

print(f"The middle number is {median}")  # F-string產生中間有可變數值的字串
