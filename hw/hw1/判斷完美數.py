x= int(input("請輸入一個整數:"))

lis=[]
sum = 0
for i in range(1,x+1):
    
    if(x%i==0):
        lis.append(i)
        
for z in range(1,x):
    
    if(x%z==0):
        sum=sum+z
        

print(x,"的因數:",lis)

i=0

while(i<len(lis)-1):
    if(i<len(lis)-1):
        print(lis[i],end='')
    if(i<len(lis)-2):
        print("+",end='')
    i=i+1
print("=%d"%(sum))

#print(lis,x,i,sum)

if(x==sum):
    print(x,"是一個完美數")
else:
    print("%d不是一個完美數"%(x))