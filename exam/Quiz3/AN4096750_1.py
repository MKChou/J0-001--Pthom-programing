

enter = input("要算排列還是組合？(P:排列, C:組合):")

while(enter != "P" and enter != "C"):
    print("請輸入P或是C")
    enter = input("要算排列還是組合？(P:排列, C:組合):")
    




if enter=="C":
    num1, num2 =input("P多少取多少(請輸入兩個正整數，以逗點分隔):").split(",")
    num1=int(num1)
    num2=int(num2)

    while(num1<num2):
        print("前者要大於者")
        num1, num2 =input("P多少取多少(請輸入兩個正整數，以逗點分隔):").split(",")
        num1=int(num1)
        num2=int(num2)

        num1, num2 =input("C多少取多少(請輸入兩個正整數，以逗點分隔):").split(",")
        

    sum1=1
    for i in range(1,num1+1):
        sum1 = sum1*i

    sum2=1
    for i in range(1,(num1-num2)+1):
        sum2 = sum2*i

    sum3=1
    for i in range(1,num2+1):
        sum3 = sum3*i

    #print(sum1,sum2,sum3)
    print("C",num1,"取",num2,"等於",int(sum1/(sum2*sum3)))

if enter=="P":
    num1, num2 =input("P多少取多少(請輸入兩個正整數，以逗點分隔):").split(",")
    num1=int(num1)
    num2=int(num2)

    while(num1<num2):
        print("前者要大於者")
        num1, num2 =input("P多少取多少(請輸入兩個正整數，以逗點分隔):").split(",")
        num1=int(num1)
        num2=int(num2)


    sum1=1
    for i in range(1,num1+1):
        sum1 = sum1*i

    sum2=1
    for i in range(1,(num1-num2)+1):
        sum2 = sum2*i

    ans=sum1/sum2

    print("P",num1,"取",num2,"等於",int(sum1/sum2))
