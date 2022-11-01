import random
enter = input("你要出甚麼拳((S)出剪刀、(R)出石頭、(P)出布，或輸入q退出)?:")
qq=0
if(enter == "S"):
    co = 1
if(enter == "R"):
    co = 2
if(enter == "P"):
    co = 3

while (1):
    if(enter == "q"):
        break

    com = random.randint(1,3)
    #print(com)

    if(co == com):
        if(co == 1):
            print("你出剪刀，我出剪刀。這局平手喔。")
        if(co == 2):
            print("你出石頭，我出石頭。這局平手喔。")
        if(co == 3):
            print("你出布，我出布。這局平手喔。")

    if(co == 1):
        if(com == 2):
            print("你出剪刀，我出石頭。是我贏了 嘻嘻^_^")
        if(com == 3):
            print("你出剪刀，我出布。是我輸了QQ")

    if(co == 2):
        if(com ==3 ):
            print("你出石頭，我出布。是我贏了 嘻嘻^_^")
        if(com == 1):
            print("你出石頭，我出剪刀。是我輸了QQ")
        
    if(co == 3):
            if(com ==1 ):
                print("你出布，我出剪刀。是我贏了 嘻嘻^_^")
            if(com == 2):
                print("你出布，我出石頭。是我輸了QQ")

    enter = input("你要出甚麼拳((S)出剪刀、(R)出石頭、(P)出布，或輸入q退出)??:")
    if(enter == "S"):
        co = 1
    if(enter == "R"):
        co = 2
    if(enter == "P"):
        co = 3
