from progress.progress import load_progress, load_user
from request.request_sender import send_request





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
