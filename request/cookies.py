import json


def get_cookies():
    with open("COOKIES.txt", 'r') as file:
        data = file.read()
        cookie_list = json.loads(data)
        cookie_dict = {}
        for cookie in cookie_list:
            cookie_key = cookie['name']
            cookie_value = cookie['value']
            cookie_dict[cookie_key] = cookie_value

    return cookie_dict


def get_cookies_as_header():
    cookies_dict = get_cookies()
    cookies_merged = ""
    for cookie in cookies_dict:
        cookies_merged += cookie + "=" + cookies_dict[cookie] + "; "
    return cookies_merged
