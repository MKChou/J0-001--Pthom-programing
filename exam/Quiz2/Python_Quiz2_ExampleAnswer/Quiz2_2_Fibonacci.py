n = 20  # 題目要求的值:20
fib = [1, 1]  # 初始化儲存費波納契數列的串列，前兩位是1,1

for i in range(2, n):
    fib.append(fib[i-2] + fib[i-1])  # 將前兩位的值加起來並加入到串列後面
print(fib)  # 印出做好的費波納契數列

sum = 0  # 以0初始化之後用來計算的加總值
for j in range(len(fib)):  # 遍歷fib串列的每一個元素
    sum += fib[j]  # 計算總和
print(f"費波納契數列前{n}項總和:{sum}")  # 最後輸出費波納契數列前20項總和
