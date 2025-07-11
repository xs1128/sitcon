import json

# 在這邊做些什麼才會輸出下面的東西ㄋ
# 讀取檔案 example.json

f = open("../example.json", "r")
ex_dict = json.load(f)
    
print(ex_dict) # 輸出 {'a': 1, 'b': 2, 'c': 3, 'd': 4}
