ex_list = ["a", "b", "c", "d", "e"]
ex_list2 = ["f", "g", "h", "i", "j"]

# 在這邊做些什麼才會輸出下面的東西ㄋ
# 請在這邊加入程式碼來符合題目要求

ex_list[3] = "f"

ex_list.extend(ex_list2)

print(ex_list) # 輸出 ["a", "b", "c", "f", "e", "f", "g", "h", "i", "j"]