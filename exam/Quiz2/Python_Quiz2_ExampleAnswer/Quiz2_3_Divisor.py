n = int(input("請輸入一個整數:"))  # 輸入數值，以int把輸入的數值強制轉成整數(遇到非數字會產生錯誤)

divisor = []  # 初始化儲存因數的串列
i = 0
while i < n:  # 用while迴圈來判斷小於n的所有整數是不是n的因數
    i += 1
    if n % i == 0:  # 如果n可以被i整除，則i是n的因數
        divisor.append(i)  # 將i加入儲存因數的串列
print(f"{n}的因數:{divisor}")  # 以F-string印出n所有的因數
