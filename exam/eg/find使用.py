##################

llist = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22",
"23","24","25"]
for i in range(0,len(llist)):
    if(llist[i].find("5")>0):
        print(llist[i])
    

##################

list = ["Hello ", "Middle ","World, ", "Yo Yo Man!", "Sunny, Air, Yes!", "Intelligent Robot!"]
i = 0
for i in range(0,len(list)):
    if list[i].find("o")>0 :
        print(list[i],end=" ")
    