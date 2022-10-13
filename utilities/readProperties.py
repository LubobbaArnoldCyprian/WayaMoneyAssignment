import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")
# config.read(".//Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common_info', 'baseURL')
        return url

    @staticmethod
    def get_user_email():
        username = config.get('common_info', 'user_email')
        return username

    @staticmethod
    def get_password():
        password = config.get('common_info', 'password')
        return password

    @staticmethod
    def get_post():
        post = config.get('common_info', 'post')
        return post

