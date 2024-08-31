import requests

from auth import get_bearer
from headers import headers


def get_crew_id_by_name(name):
    response = requests.get(f"https://scapi.rockstargames.com/crew/byname?name={name}", headers=headers())
    response = response.json()
    return response['crewId']

def get_users(crewId):
    for i in range(5):
        response = requests.get(f"https://scapi.rockstargames.com/crew/rankMembership?crewId={crewId}&rankOrder={i}&onlineService=sc&searchTerm=&pageIndex=0&pageSize=1000", headers=headers())
        response = response.json()
        for user in response['rankMembers']:
            with fop
            print(user["nickname"])