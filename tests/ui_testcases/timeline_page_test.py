import allure
from page_objects.login_page import LoginPage
from page_objects.timeline_page import TimeLinePage
from tests.base_test import BaseTest
from application_settings.application_settings import ApplicationSettings


class TimeLinePageTest(BaseTest):

    application_settings = ApplicationSettings()
    data = application_settings.get_test_data_from_excel("login", "login_data")

    @allure.title("Timeline Page - Sanity Test")
    @allure.description("Checking if a user can post normal text on timeline")
    def test_01_post_text_successfully(self):
        timeline_page = TimeLinePage(self.driver)
        print("Starting to test text posting functionality")
        assert timeline_page.post_text_successfully() is True, "text posting failed"

    # @allure.title("Login Page - Sanity Test")
    # @allure.description("Checking if login work with invalid credentials")
    # def test_02_login_functionality_invalid_email(self):
    #     login_page = LoginPage(self.driver)
    #     print("Starting to check login functionalities")
    #     assert login_page.login_with_invalid_credentials_failed() is True, "Logged in with invalid credentials, " \
    #                                                                        "Something is wrong"
