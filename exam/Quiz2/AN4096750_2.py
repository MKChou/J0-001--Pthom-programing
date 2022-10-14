def fib(n):                         
    if n>1:                       
        return fib(n-1) + fib(n-2)  
    return n

a=[]

sum=0
for i in range(21):                 
    #print(fib(i), end = ',')
    a.append(fib(i))
    sum=sum+fib(i)
    

print(a)
print("費波那契數列前20項總和：",sum)