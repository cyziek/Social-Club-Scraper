import json
import time

import requests

from request.cookies import get_cookies
from request.headers import get_headers


def get_bearer():
    with open("bearer.txt", 'r') as file:
        bearer = file.readline()
    return bearer


def refresh_token():
    try:
        attempt = 0
        response = requests.post('https://www.rockstargames.com/auth/ping-bearer.json', headers=get_headers(),
                                 timeout=10)
        while attempt < 3 and response.status_code != 200:
            time.sleep(5)
            attempt += 1
            response = requests.post('https://www.rockstargames.com/auth/ping-bearer.json',
                                     headers=get_headers(), timeout=10)
    except requests.exceptions.Timeout:
        return print(
            "\n\n\nTwoje cookiesy wygasły (ping-bearer timeout)! Zaloguj się w przeglądarce i wyeksportuj pliki cookies do pliku request/COOKIES.txt\n\n\n")
    ##


    if response.status_code == 200 and response.json()['bearerToken'] != False:
        bearer_value = response.json()
        bearer_value = bearer_value['bearerToken']
        with open("request/bearer.txt", "w") as bearer_file:
            bearer_file.write(bearer_value)
        return
