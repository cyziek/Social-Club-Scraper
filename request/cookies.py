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

def upsert_cookie(domain, name, value, path, expirationDate, secure, sameSite):
    with open('COOKIES.TXT', 'r') as file:
        existing_cookies = json.load(file)
    found = False
    for cookie in existing_cookies:
        if cookie['domain'] == domain and cookie['name'] == name and cookie['path'] == path:
            cookie['value'] = value
            found = True
            break
    if not found:
        new_cookie = {
            "domain": domain,
            "hostOnly": False,
            "httpOnly": False,
            "name": name,
            "path": path,
            "sameSite": None,
            "secure": secure,
            "session": True,
            "storeId": None,
            "value": value
        }
        if expirationDate:
            new_cookie["expirationDate"] = expirationDate
        if secure:
            new_cookie["secure"] = secure

        existing_cookies.append(new_cookie)

    with open('COOKIES.TXT', 'w') as f:
        json.dump(existing_cookies, f, indent=4)
