import json
import logging
from core.const import UserType, UsersJsonKeys
from core.exceptions import *
from core.modules.regular_user import RegularUser
from core.modules.user import User
from core.user_interface.user_input import user_information

logging.basicConfig(level=logging.INFO, filename='loggers.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def read_user_file(file_path):
    with open(file_path, 'r') as users_file:
        users = json.loads(users_file.read())
    return users


def log_in(file_path):
    user_details = user_information()
    user_name = user_details[0]
    password = user_details[1]
    existing_users = read_user_file(file_path)
    try:
        for user in existing_users["users"]:
            if user[UsersJsonKeys.USER] == user_name and user[UsersJsonKeys.PASSWORD] == password:
                if user[UsersJsonKeys.TYPE] == UserType.REGULAR:
                    logging.info('regular user logged in')
                    return RegularUser(user[UsersJsonKeys.USER], user[UsersJsonKeys.PASSWORD])
                else:
                    if user[UsersJsonKeys.TYPE] == UserType.PREMIUM:
                        logging.info('premium user logged in')
                        return User(user[UsersJsonKeys.USER], user[UsersJsonKeys.PASSWORD])
        raise InvalidLogInDetails
    except InvalidLogInDetails:
        print(InvalidLogInDetails.__name__)
    logging.info("user couldn't log in")


def sigh_up(file_path, type=UserType.REGULAR):
    user_details = user_information()
    user_name = user_details[0]
    password = user_details[1]
    new_user = {UsersJsonKeys.USER: user_name, UsersJsonKeys.PASSWORD: password, UsersJsonKeys.TYPE: type}
    existing_users = read_user_file(file_path)
    for user in existing_users["users"]:
        if user[UsersJsonKeys.USER] == user_name:
            logging.info("user already exists")
            return
    existing_users["users"].append(new_user)
    with open(file_path, 'r+') as users_file:
        json.dump(existing_users, users_file, indent=4)
    logging.info("new user sighed up")
