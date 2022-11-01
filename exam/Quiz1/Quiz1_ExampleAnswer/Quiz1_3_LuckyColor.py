color = ['紅', '橙', '黃', '綠', '藍', '靛', '紫']

date = eval(input("今天是幾號? "))

# 在F-string的大括號中計算date除7的餘數，並將該值作為color串列的索引值，得到顏色
print(f"今天的幸運色是{color[date%7]}色")
