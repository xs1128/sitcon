name = input("請輸入用戶名稱:")
name = name.replace(" ", "-")
l = len(name)

if l < 6 or l > 12:
    print(f"你的用戶名稱為:" + name.lower())
else:
    print("用戶名稱長度需介於 6 ~ 12 之間")