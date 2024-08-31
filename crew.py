from request.request_sender import send_request


def crew_members_import():
    crewId = get_crew_id()
    get_users(crewId)


def get_crew_id():
    with open("crew_name.txt", 'r', encoding="utf-8") as file:
        crew_name = file.readline()
    return get_crew_id_by_name(crew_name)


def get_crew_id_by_name(name):
    response = send_request(f"https://scapi.rockstargames.com/crew/byname?name={name}")
    response = response.json()
    return response['crewId']


def get_users(crewId):
    for i in range(5):
        response = send_request(
            f"https://scapi.rockstargames.com/crew/rankMembership?crewId={crewId}&rankOrder={i}&onlineService=sc&searchTerm=&pageIndex=0&pageSize=1000")
        response = response.json()
        for user in response['rankMembers']:
            with open("../crew_members.txt", 'a', encoding='utf-8') as file:
                file.write(str(user["nickname"]) + "\n")
