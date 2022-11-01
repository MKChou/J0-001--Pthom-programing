a, b, c = eval(input("請輸入三角形三邊長:"))  # 以eval轉換成數值值及使用多重指定(a,b,c)
sides = [a, b, c]  # 將輸入的三個數值放入sides串列
sides.sort()  # 自動由小到大排序sides串列
# print(sides)

# 若兩短邊和大於第三邊，則是三角形
if sides[0] + sides[1] > sides[2]:
    # 確認是三角形後，以畢氏定理及if...elif...else判斷是哪種三角形
    if sides[0]**2 + sides[1]**2 > sides[2]**2:  # **:表示次方
        print(f"三角形的周長為{sides[0] + sides[1] + sides[2]}, 這是銳角三角形")

    elif sides[0]**2 + sides[1]**2 < sides[2]**2:
        print(f"三角形的周長為{sides[0] + sides[1] + sides[2]}, 這是鈍角三角形")

    else:
        print(f"三角形的周長為{sides[0] + sides[1] + sides[2]}, 這是直角三角形")
else:  # 兩短邊和沒有大於第三邊，不是三角形
    print("這不是三角形的邊長")
