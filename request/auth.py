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
        response = requests.post('https://www.rockstargames.com/auth/ping-bearer.json', headers=get_headers(), timeout=5)
        while attempt < 3 & response.status_code != 200:
            time.sleep(2)
            refresh_token()
            attempt += 1
            response = requests.post('https://www.rockstargames.com/auth/ping-bearer.json',
                                     headers=get_headers(), timeout=5)
    except requests.exceptions.Timeout:
        return print(
        "\n\n\nTwoje cookiesy wygasły (ping-bearer timeout)! Zaloguj się w przeglądarce i wyeksportuj pliki cookies do pliku request/COOKIES.txt\n\n\n")
##


    with open("request/bearer.txt", "w") as bearer_file:
        bearer_value = response.json()
        bearer_value = bearer_value['bearerToken']
        bearer_file.write(bearer_value)


