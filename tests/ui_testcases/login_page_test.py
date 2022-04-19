import allure
from page_objects.login_page import LoginPage
from tests.base_test import BaseTest
from application_settings.application_settings import ApplicationSettings


class LoginPageTest(BaseTest):

    application_settings = ApplicationSettings()
    data = application_settings.get_test_data_from_excel("login", "login_data")

    email, password = data

    @allure.title("Login Page - Sanity Test")
    @allure.description("Checking if login functionalities are working properly")
    def test_01_login_functionality(self):
        login_page = LoginPage(self.driver)
        print("Starting to check login functionalities")
        assert login_page.login(self.email, self.password) is True, "Login functionality didn't work properly"

    @allure.title("Login Page - Sanity Test")
    @allure.description("Checking if login work with invalid credentials")
    def test_02_login_functionality_invalid_email(self):
        login_page = LoginPage(self.driver)
        print("Starting to check login functionalities")
        assert login_page.login_with_invalid_credentials_failed() is True, "Logged in with invalid credentials, " \
                                                                           "Something is wrong"
