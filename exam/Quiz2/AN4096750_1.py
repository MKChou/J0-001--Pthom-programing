
n=int(input("請輸入飯糰的數量(2~20):"))

while(n>20 or n<2):
    print("數值超出範圍")
    n=int(input("請輸入飯糰的數量(2~20):"))


for x in range(1,n+1):
    print(" "*(n-x)+"*"*(x*2-1))