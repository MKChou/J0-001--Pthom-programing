a,b,c = input("Input three number").split()


a = int(a)
b=int(b)
c=int(c)

ddd = [a,b,c]

if c>a:
        t=a;
        a=c;
        c=t;
if(b>a):
        t=b;
        b=a;
        a=t;

if(c>b):
        t=c;
        c=b;
        b=t;


print(ddd)

print(a,b,c)
if c>b+a or b>a+c or a>b+c:
    print("這不是三角形的邊長")
elif c*c+b*b == a*a:
        print("直角三角形")
elif c*c+b*b > a*a:
        print("銳角三角形")
elif c*c+b*b < a*a: 
        print("鈍角三角形")

