import json

ex_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}

# 做什麼才能存檔呢？
# 請在這邊加入程式碼來符合題目要求
with open("ex_dict.json", "w") as f:
    json.dump(ex_dict, f, indent=4)