password = "SITCON"

while True:
    user_input = input("請輸入密碼:")
    if user_input == password:
        break
    print("您輸入的密碼有錯，請再試一次\n")
print("密碼正確")