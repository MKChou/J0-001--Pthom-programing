import random
a = 1
i = 1
country = [["楚"],["漢"]]

#b1 = random.randint(50,100)

country[0].append(random.randint(50,100))
country[0].append(random.randint(0,100))
country[1].append(random.randint(50,100))
country[1].append(random.randint(0,100))

print("楚 hp:%d  atk:%d"%(country[0][1],country[0][2]))
print("漢 hp:%d  atk:%d"%(country[1][1],country[1][2]))


han_HP=country[1][1]-country[0][2]
tu_HP=country[0][1]-country[1][2]
country[1][1]=han_HP
country[0][1]=tu_HP



while(i<99):
    print("----------------------------Round:%d"%(i))
    i = i+1
    print("楚 attack 漢")
    print("漢 reamin %d"%(han_HP))
    print("漢 attack 楚")
    print("楚 reamin %d"%(tu_HP))
    
    if(han_HP<=0 or tu_HP<=0):
        if (han_HP == tu_HP):
            print("\n平手")
        elif(han_HP > tu_HP):
            print("\n漢 Win")
        else:
            print("\n楚 Win")
        break
    han_HP=country[1][1]-country[0][2]
    tu_HP=country[0][1]-country[1][2]
    country[1][1]=han_HP
    country[0][1]=tu_HP
