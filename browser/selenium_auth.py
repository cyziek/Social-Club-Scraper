import json

from playwright.sync_api import sync_playwright


def open_browser_and_refresh_session():
    with sync_playwright() as p:
        url = "https://socialclub.rockstargames.com/"
        browser = p.chromium.launch(headless=False, args=['--disable-blink-features=AutomationControlled'])
        agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.81"
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

