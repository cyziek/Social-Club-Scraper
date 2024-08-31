def get_bearer():
    with open("bearer.txt", 'r') as file:
        bearer = file.readline()
    return bearer
