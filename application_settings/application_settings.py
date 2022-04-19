"""
  Application Settings class implementation.
  Author: Shampad, Date: March 13, 2022
"""

import datetime
from utils.excel_utils import read_configuration_data_from_excel, read_data_from_excel_by_row
from utils.json_utils import json_reader


class ApplicationSettings:
    """
    This class is used to store the application settings.
    """
    file_ext = ".exe"
    browser_name = "chrome"
    image_folder_path = None
    start_time = datetime.datetime.now()
    configuration_file_path = "./config.json"

    # Environment details
    environment_type = "qa"
    url = ''
    test_data_file_path = "./test_data/{}_test_data.xlsx".format(environment_type)

    def setUp(self, os="win", environment="qa"):

        data_file = "./test_data/{}_test_data.xlsx".format(environment)
        data = read_configuration_data_from_excel(data_file, sheet_name="configuration")

        if os is not None and os.lower() == "win":
            self.file_ext = ".exe"
        else:
            self.file_ext = ""

        self.browser_name = data['browser']

        self.environment_type = environment
        self.url = data['frontend_url']

    def get_browser_name(self):
        return self.browser_name.lower()

    def get_test_url(self):
        return self.url

    def get_image_folder_path(self):
        return self.image_folder_path

    def get_start_time(self):
        return self.start_time

    def get_file_ext(self):
        return self.file_ext

    def set_browser_name(self, browser_name):
        self.browser_name = browser_name

    def set_url(self, url):
        self.url = url

    def set_image_folder_path(self, image_folder_path):
        self.image_folder_path = image_folder_path

    def get_test_data_from_excel(self, sheet_name, table_name):
        """
        returns the test data from excel sheet based on the table name
        :param sheet_name:
        :param table_name:
        :return:
        """
        return read_data_from_excel_by_row(self.test_data_file_path, sheet_name, table_name)

    @staticmethod
    def get_login_credentials_table_name():
        return "login_test"

    @classmethod
    def get_signup_data_table_name(cls):
        return "signup"

    def get_configuration_file_path(self):
        """
        returns current configuration file path "./config.json"
        :return:
        """
        return self.configuration_file_path

    def get_base_configuration(self):
        """
        returns the current environment type declared in the config.json file
        :return:
        """
        return json_reader(self.get_configuration_file_path())["settings"]["environmentType"]

    def get_test_data_file_path(self):
        """
        returns current test data file path
        :return:
        """
        return self.test_data_file_path

    def get_test_data_file(self):
        """
        returns current test data file path
        :return:
        """
        return "./test_data/{}_test_data.xlsx".format(self.get_base_configuration())

    def get_api_base_url(self):
        """
        get api base url based on current test environment
        :return:
        """
        file_path = self.get_test_data_file()
        return read_configuration_data_from_excel(file_path)["api_url"]
