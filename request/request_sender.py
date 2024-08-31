import time

import requests

from request.auth import refresh_token
from request.headers import get_headers


def send_request(url):
    attempt = 0
    response = None
    headers = get_headers()
    try:
        response = requests.get(url, headers=headers, timeout=10)
        while attempt < 3 & response.status_code != 200:
            time.sleep(1)
            refresh_token()
            attempt += 1
            response = requests.get(url, headers=headers, timeout=10)
    except requests.exceptions.Timeout:
        print(
            "\n\n\nTwoje cookiesy wygasły! Zaloguj się w przglądarce i wyeksportuj pliki cookies do pliku request/cookies.txt\n\n\n")

    return response
