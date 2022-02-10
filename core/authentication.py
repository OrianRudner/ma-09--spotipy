import json
from core.const import UserType
from core.modules.regular_user import RegularUser


def read_user_file(file_path):
    with open(file_path, 'r') as users_file:
        users = json.loads(users_file.read())
    return users


def log_in(user_name, password, file_path):
    existing_users = read_user_file(file_path)
    for user in existing_users["users"]:
        if user["user"] == user_name and user["password"] == password:
            if user["type"] == UserType.REGULAR:
                return RegularUser(user["user"], user["user"])
            else:
                if user["type"] == UserType.PREMIUM:
                    return RegularUser(user["user"], user["user"])
    return False


def sigh_up(user_name, password, file_path, type="regular"):
    new_user = {"new_user": user_name, "password": password, "type": type}
    existing_users = read_user_file(file_path)
    for user in existing_users["users"]:
        if user["user"] == user_name:
            return
    existing_users["users"].append(new_user)
    with open(file_path, 'r+') as users_file:
        json.dump(existing_users, users_file, indent=4)
