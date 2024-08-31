from requests.api_requests import get_users
from crew import get_crew_id

if __name__ == '__main__':
    crewId = get_crew_id()
    get_users(crewId)