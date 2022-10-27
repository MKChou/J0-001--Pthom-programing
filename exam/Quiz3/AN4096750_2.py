clock = int(input("現在幾點?"))

while(clock<0 or clock>=24):
    clock = int(input("現在幾點?"))

fa = {0,17,18,19,20,21,22,23}
se = {10,11,12,13,14,15,16,17,20,21,22,23,0,1,2,3,0}

for i in  fa:
    if i ==clock:
        a=1

for i in  se:
    if i ==clock:
        b=1

if (a==1):
    print("全家",end="")

if(a==1 and b==1):
    print("、",end="")


if (b==1):
    print("7-11")
