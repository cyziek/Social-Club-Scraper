import json
import time
from playwright.sync_api import sync_playwright
from request.cookies import upsert_cookie
import os

def open_browser_and_refresh_session():
    with sync_playwright() as p:
        url = "https://socialclub.rockstargames.com/"
        browser = p.chromium.launch(headless=False, args=['--disable-blink-features=AutomationControlled'])
        agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.81"
        context = browser.new_context(user_agent=agent)

        # with open("COOKIES.txt", 'r') as init_state_file:
        #     manual_cookies = json.load(init_state_file)
        #     for cookie in manual_cookies:
        #         if 'sameSite' in cookie:
        #             if cookie['sameSite'] == 'lax':
        #                 cookie['sameSite'] = 'Lax'
        #             elif cookie['sameSite'] is None:
        #                 cookie['sameSite'] = 'None'
        #             elif cookie['sameSite'] == 'strict':
        #                 cookie['sameSite'] = 'Strict'
        # with open("state.json", 'r') as state_file:
        #     cookies_from_state = json.load(state_file)
        #     cookies_from_state['cookies'] = manual_cookies
        # with open("state.json", 'w') as state_file_w:
        #     json.dump(cookies_from_state, state_file_w)
        context = browser.new_context(storage_state="state.json", user_agent=agent)
        page = context.new_page()

        page.goto(url)
        print(page.title())
        title = ""
        while "Feed" not in title:
            page.wait_for_timeout(1000)
            title = page.title()

        page.goto(url)
        page.wait_for_timeout(5000)

        context.storage_state(path="state.json")
        context.close()
        browser.close()
        with open("request/bearer.txt", 'w') as bearer_write:
            with open("COOKIES.txt", 'w') as file_write:
                with open("state.json", 'r') as state_file:
                    cookies_from_state = json.load(state_file)
                    cookies_from_state = cookies_from_state['cookies']
                    for cookie in cookies_from_state:
                        if "BearerToken" in cookie['name']:
                            bearer_write.write(cookie['value'])
                    json.dump(cookies_from_state, file_write)

                    print(cookies_from_state)





    # with open('COOKIES.txt', 'r') as file:
    #     cookies = json.load(file)
    #     for cookie in cookies:
    #         cookie_dict = {
    #             'name': cookie['name'],
    #             'value': cookie['value'],
    #             'domain': '.rockstargames.com',
    #             'path': cookie.get('path'),
    #             'secure-only-flag': cookie.get('secure'),
    #             'http-only-flag': cookie.get('httpOnly'),
    #             # 'sameSite': cookie.get('sameSite', 'Lax'),  # Defaulting sameSite to 'Lax'
    #         }
    #         driver.add_cookie(cookie_dict)
    # for i in range(2):
    #     some_element_wait_helper = driver.find_element(By.ID, 'page')
    #     wait = WebDriverWait(driver, timeout=10)
    #     try:
    #         wait.until(lambda d: some_element_wait_helper.is_displayed())
    #     except:
    #         selenium.common.exceptions.NoSuchElementException
    #     print("Twoje cookiesy wygasły! Wklej nowe do pliku COOKIES.txt...")
    #     driver.refresh()
    #     time.sleep(2)
    # fetched_cookies = driver.get_cookies()
    # for fetched_cookie in fetched_cookies:
    #     upsert_cookie(fetched_cookie['domain'], fetched_cookie['name'], fetched_cookie['value'], fetched_cookie['path'],
    #                   fetched_cookie['expiry'], fetched_cookie['secure'], fetched_cookie['sameSite'])
    # driver.quit()
