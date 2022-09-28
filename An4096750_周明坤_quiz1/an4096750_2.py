a, b, c = input("Input three number ").split()

a = int(a)
b = int(b)
c = int(c)

max = a

if c > a:
    t = a
    a = c
    c = t
if(b > a):
    t = b
    b = a
    a = t

if(c > b):
    t = c
    c = b
    b = t


print("The middle number is ", b)
