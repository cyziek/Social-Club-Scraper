import time

from browser.selenium_auth import open_browser_and_refresh_session
from crew.crew import crew_members_import
from progress.progress import load_progress, save_progress
from request.auth import refresh_token
from request.cookies import get_cookies_as_header
from stats.player_stats import *

if __name__ == '__main__':
    crew_members_import()
    with open("./output/crew_members.txt", 'r') as file:
        all_users = file.read().splitlines()

        while load_progress() <= len(all_users)-1:
            user = all_users[load_progress()]

            last_seen_date = get_user_last_seen_date(user)
            if "-" in last_seen_date:
                user_platforms = get_user_platforms(user)
            else:
                user_platforms = ";;;;;"
            with open("./output/player_stats.txt", 'a') as file_last_seen:
                file_last_seen.write(user + ";" + last_seen_date + ";"+ user_platforms +"\n")
                print(user + ";" + last_seen_date + ";" + user_platforms + "\n")
            save_progress(load_progress()+1)
            time.sleep(15)

