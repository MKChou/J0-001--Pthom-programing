# 建立每個月各有幾天的字典，key可以用字串或整數，這裡以字串示範
dayNumber = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30,
             '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}

date1 = input("請輸入日期")  # 輸入日期(格式:月份/日期)

month, day = date1.split("/")  # 透過split將date1以"/"作為分隔符分成前面的月份跟後面的日期
month = int(month)  # 把字串轉成整數
day = int(day)  # 把字串轉成整數

# 防呆條件:基本款
if "/" in date1:  # 確認字串中有"/":輸入的是日期
    if str(month) in dayNumber:  # 如果月份有在dayNumber字典中，因為字典的key是用字串格式，所以要再轉成字串
        if day <= dayNumber[str(month)]:  # 確認輸入的日期小於等於該月的天數
            # print("ok") # 測試用，確認輸入可以進入日期計算的部分
            delta = 0  # 初始化用來儲存日期間隔的變數
            delta += dayNumber[str(month)]-day  # 先算日期跟該月天數的差
            for i in range(12, month, -1):  # 再把後續月份的天數加上去
                delta += dayNumber[str(i)]
            print(delta)  # 輸出總間隔天數
        else:
            print("請輸入正確日期")  # 若日期大於該月天數，日期輸入錯誤
    else:
        print("請輸入正確月份")  # 若月份不在字典中，月份輸入錯誤
else:
    print("請輸入正確日期格式")  # 字串中沒有"/"，日期格式錯誤
