a = input("請輸入現在幾點?")  # 輸入整點時刻(0~23)
a = int(a)  # 字串轉為整數
# 7-11的優惠時間，以集合儲存(用大括弧包起來，中間沒有冒號)
seven = {0, 1, 2, 3, 10, 11, 12, 13, 14, 15, 16, 17, 20, 21, 22, 23}
# 全家的優惠時間
family = {17, 18, 19, 20, 21, 22, 23, 0}
# 先取交集找出都有優惠的時間，並存成集合both。也可以寫成seven.intersection(family)
both = seven & family

# 取7-11跟全家的差集，留下只有7-11有的時刻
if a in seven - family:  # 也可以寫成seven.difference(family)
    print("7-11")
# 取全家跟7-11的差集，留下只有全家有的時刻
elif a in family - seven:  # 也可以寫成family.difference(seven)
    print("全家")
elif a in both:
    print("7-11、全家")
else:
    print("沒有")
