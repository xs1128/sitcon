password = "SITCON"

while True:
    user_input = input("請輸入密碼:")
    if user_input == password:
        break
    print("您輸入的密碼，請在試 一次")
print("密碼正確")