import configparser
from core.authentication import *
from core.user_interface import console


def main():
    config = configparser.ConfigParser()
    config.read('config.properties')
    paths = config['Path']
    users_file_path = paths['users_file']
    user = log_in(users_file_path)
    console.run_menu(user)


if __name__ == '__main__':
    main()
