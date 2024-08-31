from requests.api_requests import get_crew_id_by_name


def get_crew_id():
    with open("crew_name.txt", 'r', encoding="utf-8") as file:
        crew_name = file.readline();
    return get_crew_id_by_name(crew_name)
