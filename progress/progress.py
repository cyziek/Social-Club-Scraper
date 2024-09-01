import json

progress_path = "./progress/progress.json"
crew_path = "./output/crew_members.txt"

def load_progress():
    try:
        with open(progress_path) as file:
            progress_data = json.load(file)
            return progress_data["user_index"]
    except (FileExistsError, FileNotFoundError, json.decoder.JSONDecodeError):
        save_progress(0)
        return 0

def load_user():
    with open(crew_path, 'r') as file:
        users = file.read().splitlines()
    return users

def save_progress(user_index):
    user_progress = {"user_index": user_index}
    with open(progress_path, 'w') as file:
        json.dump(user_progress, file)
