from html_parse.html_parser import has_current_platform_from_html
from progress.progress import load_progress, load_user
from request.request_sender import send_request
from bs4 import BeautifulSoup


def get_user_last_seen_date(user):
    gamesOwned = ""
    response = send_request(
        f"https://scapi.rockstargames.com/profile/getprofile?nickname={user}&maxFriends=0")
    response = response.json()
    lastSeen = "Unknown"
    try:
        gamesOwned = response['accounts'][0]['rockstarAccount']['gamesOwned']
    except:
        pass
    for i in gamesOwned:
        if i["name"] == "GTAV":
            lastSeen = i["lastSeen"]
            lastSeen = lastSeen.split("T")[0]
            if len(lastSeen) < 4:
                lastSeen = "Unknown"
    return lastSeen


def get_user_platforms(user):
    platforms = {"pc": " ", "ps4": " ", "ps5": " ", "xboxone": " ", "xboxsx": " "}
    return_platforms = ""
    for platform in platforms:
        response = send_request(
            f"https://socialclub.rockstargames.com/member/{user}/games/gtav/{platform}/career/overview/gtaonline"
        )
        platforms[platform] = has_current_platform_from_html(response.text)
        return_platforms += platforms[platform] + ";"

    return return_platforms
