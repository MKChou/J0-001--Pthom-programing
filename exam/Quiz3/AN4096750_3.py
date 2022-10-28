from cmath import exp

d = {1:31,
     2:28,
     3:31,
     4:30,
     5:31,
     6:30,
     7:31,
     8:31,
     9:30,
     10:31,
     11:30,
     12:31}

try:
    mon, day = input("請輸入2022的日期(a/b):").split("/")
    mon = int(mon)
    day = int(day)

    while(mon<1 or mon>12 or day<1 or day>d[mon]):
        mon, day = input("請輸入2022的日期(a/b):").split("/")
        mon = int(mon)
        day = int(day)

    sum=0
    for i in range (mon+1,13):
        sum = sum+d[i]
    sum2 = d[mon]-day
    ans = sum+sum2

    print(ans)


except:
    print("請輸入整數喔！")