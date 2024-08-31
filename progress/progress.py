import json

progress_path = "./progress/progress.json"
def load_next_user():
    with open(progress_path) as file:
        user = file.read().splitlines()
        return user
def save_progress(user_index):
    user_progress = {"user_index": user_index}
    with open(progress_path) as file:
        json.dump(user_progress, file)