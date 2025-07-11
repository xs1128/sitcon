import json
 
ex_dict = {
  "morning": {
    "food": "bread",
    "drink": "milk",
    "calories": "185"
  },
  "lunch": {
    "food": "spaghetti",
    "drink": "milk_tea",
    "calories": "900"
  },
  "dinner": {
    "food": "curry_rice",
    "drink": "orange_juice",
    "calories": "810"
  }
}

# Replace the single quotes at the string literal
json_string = json.dumps(ex_dict)
ex_dict = json.loads(json_string)
print(ex_dict)