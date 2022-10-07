'''
剉冰配料挑選器:
    你來到一家特別的剉冰店，看到招牌上有好多配料，如以下串列所
    示 Ingredients =['紅豆','大紅豆','芋頭','綠豆','粉圓','米苔目','花生','愛
    玉','仙草','芋圓','粉粿','小湯圓','布丁']，因為實在是太多配料了不知
    道該怎麼挑選。所以請寫一個程式，輸入你學號的後四碼，程式將
    會把每一碼作為索引值將該元素彈出(pop)列表，這些彈出的元素即
    為你的剉冰配料，最後請輸出這些配料。
'''
Ingredients =['紅豆','大紅豆','芋頭','綠豆','粉圓','米苔目','花生','愛玉','仙草','芋圓','粉粿','小湯圓','布丁']

number1,number2,number3,number4 = input("Please Enter your studenr ID(A,B,C,D): ").split(',')
number1 = int(number1)
number2 = int(number2)
number3 = int(number3)
number4 = int(number4)

print(Ingredients[number1],end=" ")
Ingredients.pop(number1)
print(Ingredients[number2],end=" ")
Ingredients.pop(number2)
print(Ingredients[number3],end=" ")
Ingredients.pop(number3)
print(Ingredients[number4],end=" ")


