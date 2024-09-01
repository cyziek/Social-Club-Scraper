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
        save_headers_from_response(response)
        # save_cookies_from_response(response)


def save_headers_from_response(response):
    bearer_value = response.json()
    bearer_value = bearer_value['bearerToken']

    response_cookies = response.cookies
    with open("request/bearer.txt", "w") as bearer_file:
        bearer_file.write(bearer_value)
    return


def save_cookies_from_response(response):
    new_cookies = {}

    with open('COOKIES.TXT', 'r') as file:
        existing_cookies = json.load(file)
    for cookie in response.cookies:
        new_cookies[cookie.name] = cookie.value
        upsert_cookie(existing_cookies, cookie.domain, cookie.name, cookie.value, cookie.path, cookie.expires, cookie.secure)
    #
    # for name, value in new_cookies.items():
    #     upsert_cookie(existing_cookies, domain, name, value, path)

    # with open('cookies.json', 'w') as f:
    #     json.dump(existing_cookies, f, indent=4)
    #
    # for name, value in new_cookies.items():
    #     upsert_cookie(existing_cookies, domain, name, value, path)


def upsert_cookie(existing_cookies, domain, name, value, path, expirationDate, secure):
    found = False
    for cookie in existing_cookies:
        if cookie['domain'] == domain and cookie['name'] == name and cookie['path'] == path:
            cookie['value'] = value
            found = True
            break
    if not found:
        # If the cookie does not exist, append a new one
        existing_cookies.append({
            "domain": domain,
            "expirationDate": expirationDate,
            "hostOnly": False,
            "httpOnly": False,
            "name": name,
            "path": path,
            "sameSite": None,
            "secure": secure,
            "session": True,
            "storeId": None,
            "value": value
        })

    with open('COOKIES.TXT', 'w') as f:
        json.dump(existing_cookies, f, indent=4)
