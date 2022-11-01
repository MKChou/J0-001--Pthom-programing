def fractorial(x):  # 定義階乘函數
    x = int(x)  # 先把參數輸入x轉成整數
    if x == 0:  # 0階乘 = 1
        return 1  # 返回值1
    else:  # 輸入不為0的其他狀況
        fact = 1  # 初始化用來儲存乘積的變數
        while(x > 1):   # 當輸入值大於1則執行以下迴圈
            fact *= x   # fact = fact * x
            x -= 1  # 由輸入值x逐漸往下減1
        return fact  # 返回最終乘績


a = input("要算排列還是組合?(P:排列, C:組合): ")  # 輸入P或C
if a == "P":  # 輸入P則計算排列
    num1, num2 = eval(input("P多少取多少?(請輸入兩個正整數，以逗點分隔): "))  # 輸入多少取多少
    if num1 < num2:  # 前者必須大於後者，故先排除小於的情況
        print("前者要大於後者")
    else:  # 沒問題則進行計算
        # 套用剛剛定義的階乘函數以及排列的公式
        print(f"P {num1}取{num2}等於{int(fractorial(num1)/fractorial(num1-num2))}")
elif a == "C":  # 輸入C則計算組合
    num1, num2 = eval(input("C多少取多少?(請輸入兩個正整數，以逗點分隔): "))  # 輸入多少取多少
    if num1 < num2:  # 前者必須大於後者，故先排除小於的情況
        print("前者要大於後者")
    else:  # 沒問題則進行計算
        print(
            f"C {num1}取{num2}等於{int(fractorial(num1)/fractorial(num1-num2)/fractorial(num2))}")  # 套用剛剛定義的階乘函數以及組合的公式
else:  # 輸入不是P或C，則跳出錯誤訊息
    print("請輸入P或C")
