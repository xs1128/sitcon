name = input("請輸入用戶名稱:")

if len(name) < 6 or len(name) > 12:
    print("用戶名稱長度需介於 6 ~ 12 之間")
else:
    name = name.replace(" ", "-")
    print(f"你的用戶名稱為:{name.lower()}")

