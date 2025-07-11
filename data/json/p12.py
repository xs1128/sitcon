import json

ex_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}

json_dump = json.dumps(ex_dict)
json_load = json.loads(json_dump)

print(type(json_dump)) # 輸出 <class 'str'>
print(type(json_load)) # 輸出 <class 'dict'>