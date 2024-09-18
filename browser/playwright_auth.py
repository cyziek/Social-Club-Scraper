import json
import time

from playwright.sync_api import sync_playwright


def open_browser_and_refresh_session():
    with sync_playwright() as p:
        url = "https://socialclub.rockstargames.com/"
        args = ['--disable-blink-features=AutomationControlled']
        browser = p.chromium.launch(headless=True, args=args)
        agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.81"
        context = browser.new_context(storage_state="state.json", user_agent=agent)
        page = context.new_page()
        page.goto(url)

        title = ""
        elapsed_time = time.time()
        while "Feed" not in title and time.time()-elapsed_time <= 10:
            page.wait_for_timeout(1000)
            try:
                title = page.title()
                print(page.title())
            except:
                pass


        if time.time()-elapsed_time >= 10:
            browser.close()
            browser = p.chromium.launch(headless=False, args=args)

            context = browser.new_context(user_agent=agent)
            page = context.new_page()
            page.goto(url)
            while "Feed" not in title :
                page.wait_for_timeout(1000)
                try:
                    title = page.title()
                except:
                    pass

        page.wait_for_timeout(2000)

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

