import json
import logging
from core.const import UserType
from core.modules.regular_user import RegularUser

logging.basicConfig(level=logging.INFO, filename='loggers.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def read_user_file(file_path):
    with open(file_path, 'r') as users_file:
        users = json.loads(users_file.read())
    return users


def log_in(user_name, password, file_path):
    existing_users = read_user_file(file_path)
    for user in existing_users["users"]:
        if user["user"] == user_name and user["password"] == password:
            if user["type"] == UserType.REGULAR:
                logging.info('regular user logged in')
                return RegularUser(user["user"], user["user"])
            else:
                if user["type"] == UserType.PREMIUM:
                    logging.info('premium user logged in')
                    return RegularUser(user["user"], user["user"])
    logging.info("user couldn't log in")
    return False


def sigh_up(user_name, password, file_path, type="regular"):
    new_user = {"new_user": user_name, "password": password, "type": type}
    existing_users = read_user_file(file_path)
    for user in existing_users["users"]:
        if user["user"] == user_name:
            logging.info("user already exists")
            return
    existing_users["users"].append(new_user)
    with open(file_path, 'r+') as users_file:
        json.dump(existing_users, users_file, indent=4)
    logging.info("new user sighed up")
