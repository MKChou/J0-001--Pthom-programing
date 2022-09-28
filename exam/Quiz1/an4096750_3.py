day = input("今天幸運色幾號？")

day = int(day)

ans = day%7

if day>31:
    print("輸入日期錯誤")

elif ans == 1:
    print("今天幸運色是紅色")
elif ans == 2:
    print("今天幸運色是橙色")
elif ans == 3:
    print("今天幸運色是黃色")
elif ans == 4:
    print("今天幸運色是綠色")
elif ans == 5:
    print("今天幸運色是藍色")
elif ans == 6:
    print("今天幸運色是靛色")
elif ans == 0:
    print("今天幸運色是紫色")

