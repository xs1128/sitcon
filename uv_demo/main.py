import requests
import json


def main():
    url = "http://httpbin.org/post"

    headers = {
        "User-Agent": "Agent/1.0",
        "Host": "sitcon.tw",
        "Origin": "sitcon.camp",
        "My-Header": "Rand blabber"
    }

    # params = {
    #     "name": "stone",
    #     "age": 18,
    # }

    response = requests.post(url, data = "Hello, world!")

    # decode json to a python object
    response_json = response.json()

    # Cast json obj to dict obj
    formatted_json = json.dumps(response_json, indent=4, ensure_ascii=False)
    print(formatted_json)


if __name__ == "__main__":
    main()
