from numpy import append


cat = ["短褲","蛋捲","麻糊","米香","橘皮","本丸","圓仔"]

list = []

number = input("請輸入間隔數字(1~7)或n(結束遊戲):")
a=1


while( a==1):
    if(number=="n"):
        print("程式結束")
        break

    try:
        number = int(number)

        if(number>=1 and number<=7):
            #print(cat)
            i = number-1

            list.append(cat[i])
            cat.pop(i)
            #print(cat)
            #print(list,"\n")

            i=(i+number-1)%6
            #print(i)
            list.append(cat[i])
            cat.pop(i)
            #print(cat)
            #print(list,"\n")

            i=(i+number-1)%5
            #print(i)
            list.append(cat[i])
            cat.pop(i)
            #print(cat)
            #print(list,"\n")

            i=(i+number-1)%4
            #print(i)
            list.append(cat[i])
            cat.pop(i)
            #print(cat)
            #print(list,"\n")

            i=(i+number-1)%3
            #print(i)
            list.append(cat[i])
            cat.pop(i)
            #print(cat)
            #print(list,"\n")

            i=(i+number-1)%2
            #print(i)
            list.append(cat[i])
            cat.pop(i)
            #print(cat)
            #print(list,"\n")

            list.append(cat[0])
            cat.pop(0)

            print(list)
            break

        print("輸入錯誤，請重新數入")
    except:
        print("輸入錯誤，請重新數入")
    number = input("請輸入間隔數字(1~7)或n(結束遊戲):")