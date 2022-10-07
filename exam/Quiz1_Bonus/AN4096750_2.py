list = ["Hello ", "Middle ","World, ", "Yo Yo Man!", "Sunny, Air, Yes!", "Intelligent Robot!"]

i = 0
while i<len(list):
    if list[i].find("o")>0 :
        print(list[i],end=" ")
    i=i+1