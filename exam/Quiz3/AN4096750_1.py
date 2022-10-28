a = input("要算排列還是組合(P:排列,C:組合):")

while(a!="C" and a!="P"):
    print("請輸入P或C")
    a = input("要算排列還是組合(P:排列,C:組合):")


if(a=='P'):
    b,c = input("P多少取多少?(請輸入兩整數，以逗點分隔):").split(",")
    b = int(b)
    c = int(c)
    if(c>b):
        print("前者要大於後者")
    else:
        sum_b=1
        for i in range(1,b+1):
            sum_b = sum_b*i
        
        d = b-c
        sum_d=1
        for i in range(1,d+1):
            sum_d = sum_d*i
        e=int((sum_b/sum_d))
    
        print("P %d取%d等於%d"%(b,c,e))
    

if(a=='C'):
    b,c = input("C多少取多少?(請輸入兩整數，以逗點分隔):").split(",")
    b = int(b)
    c = int(c)
    if(c>b):
        print("前者要大於後者")
    else:
        sum_b=1
        for i in range(1,b+1):
            sum_b = sum_b*i
        
        d = b-c

        sum_c=1
        for i in range(1,c+1):
            sum_c = sum_c*i
        
        d = b-c
        sum_d=1
        for i in range(1,d+1):
            sum_d = sum_d*i

        e=int((sum_b/(sum_d*sum_c)))
    
        print("P %d取%d等於%d"%(b,c,e))





