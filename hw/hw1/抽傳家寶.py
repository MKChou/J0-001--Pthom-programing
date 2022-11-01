import random
white = 0
blue = 0
red = 0
count = 1


while(count !=80):
    b= random.randint(1,101)
    if(b>=2 and b<=40):
        print("抽了第%d次"%(count))
        print("you got blue")
        blue = blue+1
    if(b>=41):
        print("抽了第%d次"%(count))
        print("you got white")
        white = white+1
    if(b==1):
        print("抽了第%d次"%(count))
        print("you got red")
        print("==========================")
        print("恭喜抽中傳家寶，總共抽了%d抽，抽到白色%d個，藍色%d個"%(count,white,blue))
        red= red+1
        break
    count = count+1


while(count !=90 and red == 0):
    b= random.randint(1,101)
    if(b>=3 and b<=41):
        print("抽了第%d次"%(count))
        print("you got blue")
        blue = blue+1
    if(b>=42):
        print("抽了第%d次"%(count))
        print("you got white")
        white = white+1
    if(b<2):
        print("抽了第%d次"%(count))
        print("you got red")
        print("==========================")
        print("恭喜抽中傳家寶，總共抽了%d抽，抽到白色%d個，藍色%d個"%(count,white,blue))
        red= red+1
        break
    count = count+1


while(count !=100 and red == 0):
    b= random.randint(1,101)
    if(b>=4 and b<=42):
        print("抽了第%d次"%(count))
        print("you got blue")
        blue = blue+1
    if(b>=43):
        print("抽了第%d次"%(count))
        print("you got white")
        white = white+1
    if(b<3):
        print("抽了第%d次"%(count))
        print("you got red")
        print("==========================")
        print("恭喜抽中傳家寶，總共抽了%d抽，抽到白色%d個，藍色%d個"%(count,white,blue))
        red= red+1
        break
    count = count+1


if (count==100):
    print("抽了第100次")
    print("保底")
    print("==========================")
    print("殘念保底了，總共抽了100抽，抽到白色%d個，藍色%d個"%(white,blue))
#print(red,blue,white)