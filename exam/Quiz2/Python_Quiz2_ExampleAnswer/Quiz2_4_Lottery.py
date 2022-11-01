import random  # 引用random函式庫

listDigit = []  # 初始化一個空的listDigit串列，用來存三位隨機數字的每一位數

while True:  # 一直執行的無窮迴圈
    a = input("請問是否要抽獎?(y/n):")  # 問要不要抽獎(輸入y或n)
    if a == "y":
        num = random.randint(100, 999)  # 產生隨機三位數
        print(num)  # 印出隨機抽到的數字

        # 先將數字轉成字串(ex:123->"123")，再把字串轉成用串列儲存(ex:"123"->[1,2,3])
        listDigit = list(str(num))

        same = 0  # 初始化用來儲存判斷各個位數相同了幾次的變數
        for idx in range(len(listDigit)):  # 以For迴圈遍歷每一位數
            tmp = listDigit[idx]
            for idx2 in range(idx+1, len(listDigit)):  # 用第二個For迴圈指定要跟tmp比較的另一位數
                # print(tmp, listDigit[idx2])  # 測試用，印出比較的過程，以方便觀察same的規律
                if listDigit[idx2] == tmp:
                    same += 1  # 如果有一樣就把same+1
        print(same)  # 測試用，看所有的判斷共重複了幾次
        if same == 3:  # 根據觀察的結果決定if的條件
            print("恭喜中1獎")
        elif same == 1:
            print("恭喜中2獎")
        else:
            print("沒中，再加油吧")
    elif a == "n":
        break  # 跳出無窮迴圈
    else:
        print("請輸入y/n")
