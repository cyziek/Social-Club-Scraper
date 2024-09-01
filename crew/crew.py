import os

from request.request_sender import send_request


def crew_members_import():
    crew_name = read_crew_name_from_file()
    crew_id = get_crew_id_from_name(crew_name)
    get_users(crew_id)


def read_crew_name_from_file():
    with open("CREW_NAME.txt", 'r', encoding="utf-8") as file:
        crew_name = file.readline()
    return crew_name


def get_crew_id_from_name(name):
    response_ = send_request(f"https://scapi.rockstargames.com/crew/byname?name={name}")
    crew_id = response_.json()
    crew_id = crew_id['crewId']
    return crew_id


def get_users(crewId):

    open("./output/crew_members.txt", 'w', encoding='utf-8').close()

    for i in range(5):
        response = send_request(
            f"https://scapi.rockstargames.com/crew/rankMembership?crewId={crewId}&rankOrder={i}&onlineService=sc&searchTerm=&pageIndex=0&pageSize=1000")
        response = response.json()

        for user in response['rankMembers']:
            with open("./output/crew_members.txt", 'a', encoding='utf-8') as file:
                file.write(str(user["nickname"]) + "\n")
                print(str(user["nickname"]))
