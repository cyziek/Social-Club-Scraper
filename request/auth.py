import json

import requests

from request.headers import get_headers


def get_bearer():
    with open("bearer.txt", 'r') as file:
        bearer = file.readline()
    return bearer
def refresh_token():
    headers = {
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://socialclub.rockstargames.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://socialclub.rockstargames.com/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }

    with open("COOKIES.txt", 'r') as file:
        cookies = json.load(file)
        cookies_arr = {}
        for cookie in cookies:

            key = cookie["name"]
            value = cookie["value"]

            cookies_arr[key] = value



    response = requests.post('https://www.rockstargames.com/auth/ping-bearer.json', cookies=cookies_arr, headers=get_headers())

    with open("request/bearer.txt", "w") as bearer_file:
        bearer_value = response.json()
        bearer_value = bearer_value['bearerToken']
        bearer_file.write(bearer_value)


