import requests
import json

response = requests.get("https://sitcon.camp/2025/schedule.json")

print((response.json()["speakers"]))
# print(response)