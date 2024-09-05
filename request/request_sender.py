import time

import requests

from browser.selenium_auth import open_browser_and_refresh_session
from request.auth import refresh_token
from request.headers import get_headers


def send_request(url):
    attempt = 0
    response = None
    headers = get_headers()
    try:
        response = requests.get(url, headers=headers, timeout=5)
        while attempt < 3 and response.status_code != 200:
            time.sleep(2)
            open_browser_and_refresh_session()
            refresh_token()
            time.sleep(3)
            attempt += 1
            response = requests.get(url, headers=headers, timeout=5)
    except requests.exceptions.Timeout:
        print_err_message()
    if response.status_code == 401:
        attempt = 0
        while attempt < 2:
            print("Wystąpił błąd autoryzacji. Czekam 30 sekund i próbuję ponownie...")
            time.sleep(30)
            attempt += 1
            refresh_token()
            send_request(url)
            print_err_message()
            return Exception
    return response


def print_err_message():
    print(
        "\n\n\nTwoje cookiesy wygasły! Zaloguj się w przglądarce i wyeksportuj pliki cookies do pliku request/COOKIES.txt\n\n\n")
