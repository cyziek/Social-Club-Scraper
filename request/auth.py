import json
import time

import requests

from browser.playwright_auth import open_browser_and_refresh_session
from request.cookies import get_cookies, upsert_cookie
from request.headers import get_headers


def get_bearer():
    with open("bearer.txt", 'r') as file:
        bearer = file.readline()
    return bearer


def refresh_token():
    # try:
        attempt = 0
        # response = requests.post('https://www.rockstargames.com/auth/ping-bearer.json', headers=get_headers(),
        #                          timeout=10)

        # while attempt < 3 and response.status_code != 200:
        open_browser_and_refresh_session()
            # time.sleep(5)
            # attempt += 1
            # response = requests.post('https://www.rockstargames.com/auth/ping-bearer.json',
            #                          headers=get_headers(), timeout=10)

    # except requests.exceptions.Timeout:
    #     return print(
    #         "\n\n\nTwoje cookiesy wygasły (ping-bearer timeout)! Zaloguj się w przeglądarce i wyeksportuj pliki cookies do pliku request/COOKIES.txt\n\n\n")
    ##

    # if response.status_code == 200 and response.json()['bearerToken'] != False:
    #     save_headers_from_response(response)
    #     save_cookies_from_response(response)


def save_headers_from_response(response):
    bearer_value = response.json()
    bearer_expire = bearer_value['tokenExpiresIn']
    bearer_value = bearer_value['bearerToken']
    print(bearer_expire)



    response_cookies = response.cookies
    with open("request/bearer.txt", "w") as bearer_file:
        bearer_file.write(bearer_value)
    return


def save_cookies_from_response(response):
    new_cookies = {}

    for cookie in response.cookies:
        new_cookies[cookie.name] = cookie.value
        name = cookie.name
        value = cookie.value
        domain = getattr(cookie, 'domain', "None")
        path = getattr(cookie, 'path',  "None")
        expires = getattr(cookie, 'expires',  "None")
        secure = getattr(cookie, 'secure', False)
        sameSite = getattr(cookie, 'sameSite', "None")
        upsert_cookie(domain, name, value, path, expires, secure, sameSite)
    #
    # for name, value in new_cookies.items():
    #     upsert_cookie(existing_cookies, domain, name, value, path)

    # with open('cookies.json', 'w') as f:
    #     json.dump(existing_cookies, f, indent=4)
    #
    # for name, value in new_cookies.items():
    #     upsert_cookie(existing_cookies, domain, name, value, path)




