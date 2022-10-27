x= int(input(":"))

print(x)
lis=[]
for i in range(1,x+1):

    if(x%i==0):
        lis.append(i)
        #print(lis)

print(lis)