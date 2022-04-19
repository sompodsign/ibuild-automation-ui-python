import datetime
import random

import pytz
from randomuser import RandomUser
from uuid import uuid4
from application_settings.api_base_requests import BaseApi
from utils.email_reader import get_otp_from_email
from utils.json_utils import load_json
from utils.general_functions import get_raw_time
from collections import defaultdict


class CustomTestDataProvider:
    login_data = load_json("login_data.json")
    existing_email = "unidevgo.qa3@gmail.com"
    existing_username = "unidevgo.qa3"
    existing_password = "5946644S"
    auth_api = BaseApi("/auth/api/login")

    def get_user_token(self):

        response = self.auth_api.post_request(payload=self.get_user_sign_in_data())
        return response['response']['accessToken']

    def get_admin_token(self):
        response = self.auth_api.post_request(payload={})
        return response.json()['accessToken']

    def get_headers_with_user_token(self):
        headers_with_user_token = {'Authorization': self.get_user_token(), 'Content-Type': 'application/json',
                                   'Accept': 'application/json'}
        return headers_with_user_token

    def get_headers_with_admin_token(self):
        headers_with_admin_token = {'Authorization': self.get_admin_token(), 'Content-Type': 'application/json',
                                    'Accept': 'application/json'}
        return headers_with_admin_token

    @staticmethod
    def get_random_first_name():
        return RandomUser().get_first_name()

    @staticmethod
    def get_random_last_name():
        return RandomUser().get_last_name()

    @staticmethod
    def get_full_name():
        return RandomUser().get_full_name()

    @staticmethod
    def get_city():
        return RandomUser().get_city()

    @staticmethod
    def get_age():
        return RandomUser().get_age()

    @staticmethod
    def get_weight():
        return random.choice(range(1, 100))

    @staticmethod
    def get_random_number():
        return random.randint(1, 10)

    @staticmethod
    def get_random_id():
        return str(uuid4())

    @staticmethod
    def get_sex():
        return random.choice(["Male", "Female"])

    @staticmethod
    def get_headers():
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        return headers

    def current_user_id(self):
        response = self.auth_api.post_request(payload=self.get_user_sign_in_data())
        return response.json()['userId']

    def get_valid_sign_in_password(self):
        return self.login_data["valid_login_data"]["password"]

    def get_user_sign_in_data(self):
        return {"email": self.login_data["valid_login_data"]["email"], "password": self.get_valid_sign_in_password()}

    def get_registered_email(self):
        return self.login_data["valid_login_data"]["email"]

    def get_registered_password(self):
        return self.login_data["valid_login_data"]["password"]

    def get_email_for_otp_send(self):
        return {"email": self.get_existing_email()}

    def get_non_registered_email_object_for_otp_send(self):
        return {"email": self.get_new_email()}

    @staticmethod
    def get_invalid_email_object_for_otp_send():
        return {"email": "invalid_email"}

    def get_sign_in_data_without_email(self):
        return self.login_data["no_email_data"]

    def get_sign_in_data_without_password(self):
        return self.login_data["no_password_data"]

    @staticmethod
    def get_new_username():
        new_username = "unidev" + get_raw_time()
        return new_username

    @staticmethod
    def get_new_email():
        new_email = "unidev" + get_raw_time() + "@gmail.com"
        return new_email

    @staticmethod
    def get_new_password():
        new_password = "unidev" + get_raw_time()
        return new_password

    @staticmethod
    def get_6_digit_easy_numeric_password():
        return "123456"

    @staticmethod
    def get_6_digit_easy_alphanumeric_password():
        return "abc123"

    @staticmethod
    def get_6_digit_easy_alphanumeric_password_with_special_characters():
        return "abc123!"

    @staticmethod
    def get_6_digit_hard_alpha_num_sym_password():
        return "xfdK45"

    @staticmethod
    def get_8_digit_hard_alpha_num_sym_password():
        return "xfdK45a!"

    @staticmethod
    def get_8_digits_hard_password():
        return "594664a!"

    @staticmethod
    def get_8_digit_easy_password():
        return "12345678"

    @staticmethod
    def get_8_digit_easy_password_with_special_characters():
        return "12345678!"

    @staticmethod
    def get_14_digit_hard_password():
        return "594664a!@#$%^&*"

    def get_existing_username(self):
        return self.existing_username

    def get_existing_email(self):
        return self.existing_email

    def get_existing_email_object(self):
        return {"email": self.existing_email}

    def get_new_valid_register_data(self):
        return {
            "username": self.get_new_username(),
            "email": self.get_new_email(),
            "password": self.get_8_digits_hard_password()
        }

    def get_new_register_data_with_existing_username(self):
        new_admin = defaultdict()
        new_admin["username"] = self.get_existing_username()
        new_admin["email"] = self.get_new_email()
        new_admin["password"] = self.get_8_digits_hard_password()
        return new_admin

    def get_new_register_data_with_existing_email(self):
        new_admin = defaultdict()
        new_admin["username"] = self.get_new_username()
        new_admin["email"] = self.get_existing_email()
        new_admin["password"] = self.get_8_digits_hard_password()
        return new_admin

    def get_new_register_data_with_existing_username_and_email(self):
        new_admin = defaultdict()
        new_admin["username"] = self.get_existing_username()
        new_admin["email"] = self.get_existing_email()
        new_admin["password"] = self.get_8_digits_hard_password()
        return new_admin

    def get_new_register_data_with_existing_username_and_email_and_password(self):
        new_admin = defaultdict()
        new_admin["username"] = self.get_existing_username()
        new_admin["email"] = self.get_existing_email()
        new_admin["password"] = self.get_8_digits_hard_password()
        return new_admin

    def get_new_register_data_without_username(self):
        new_admin = defaultdict()
        new_admin["email"] = self.get_new_email()
        new_admin["username"] = ""
        new_admin["password"] = self.get_8_digits_hard_password()
        return new_admin

    def get_new_register_data_without_email(self):
        new_admin = defaultdict()
        new_admin["username"] = self.get_new_username()
        new_admin["email"] = ""
        new_admin["password"] = self.get_8_digits_hard_password()
        return new_admin

    def get_new_register_data_without_password(self):
        return {
            "username": self.get_new_username(),
            "email": self.get_new_email(),
            "password": ""
        }

    def get_new_register_data_without_username_and_email(self):
        return {
            "username": "",
            "email": "",
            "password": self.get_8_digits_hard_password()
        }

    def get_otp(self):
        return get_otp_from_email({"email": self.get_existing_email(), "password": self.existing_password})

    @staticmethod
    def get_invalid_otp():
        return {"otp": "1234"}

    @staticmethod
    def get_invalid_email():
        return "testemailgamil.com"

    @staticmethod
    def get_random_time():
        time_now = datetime.datetime.now(tz=pytz.timezone("Asia/Dhaka"))
        return str(time_now + datetime.timedelta(days=3))
