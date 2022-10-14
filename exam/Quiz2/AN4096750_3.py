numbers = [];

enter = input("請輸入一個整數:")
try:
    enter = int(enter)

    for i in range(1,enter+1):
        if (enter%i)==0:
            numbers.append(i)
        continue

    print(enter,"的因數:",numbers)
except:
    print ("請輸入整數：")


