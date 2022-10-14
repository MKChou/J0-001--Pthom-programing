import random

a = "1"
bingo_number = random.randint(100,999)
print(bingo_number)
enter1 = input("請問是否要抽獎(y/n):")

while( a=="1" ):
    if enter1=="y":
        enter2 = int(input("number:"))
        if( enter2==bingo_number):
            print("恭喜中1獎")
            break
        elif(int(enter2/10)==int(bingo_number/10)):
            print("恭喜中2獎")
            break
        elif(enter2%10==bingo_number%10 and int(enter2/100) ==int(bingo_number/100)):
            print("恭喜中2獎")
            break
        elif(enter2%100==bingo_number%100):
            print("恭喜中2獎")
            break
        else:
            print("沒中，再加油吧")
            enter1 = input("請問是否要抽獎(y/n):")
    elif( enter1=="n"):
        #print("結束")
        break
    else:
        print("請輸入y/n")
        enter1 = input("請問是否要抽獎(y/n):")
        
 