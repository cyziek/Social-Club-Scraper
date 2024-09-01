import time

import requests

from request.auth import refresh_token
from request.headers import get_headers


def send_request(url):
    attempt = 0
    response = None
    headers = get_headers()
    refresh_token()
    time.sleep(1)
    try:
        response = requests.get(url, headers=headers, timeout=5)
        while attempt < 3 & response.status_code != 200:
            time.sleep(1)
            refresh_token()
            attempt += 1
            response = requests.get(url, headers=headers, timeout=5)
    except requests.exceptions.Timeout:
        print_err_message()
    if response.status_code == 401:
        print_err_message()
        return Exception
    return response


def print_err_message():
    print(
        "\n\n\nTwoje cookiesy wygasły! Zaloguj się w przglądarce i wyeksportuj pliki cookies do pliku request/COOKIES.txt\n\n\n")
