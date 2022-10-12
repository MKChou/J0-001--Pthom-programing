a = input("請輸入一個整數:")

#a.isdigit()


q=str(a.isdigit())

fac = [1,] 
b=int(a)
print(q)

'''
if q == False:
    print("xxx")

else:'''

for i in range(2, b): 
        if b % i == 0:
            fac.append(i) 
            continue
        
fac.append(b)
print(fac)

