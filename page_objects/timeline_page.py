import time

from selenium.webdriver.common.by import By

from data_provider.test_data_provider import CustomTestDataProvider
from page_objects.base_page import BasePage
from helper.driver_actions import DriverActions
from helper.driver_waits import DriverWaits
from page_objects.login_page import LoginPage
from utils.logger import CustomLogger

logger = CustomLogger("login_page_log").get_logger()


class TimeLinePage(BasePage, DriverActions, DriverWaits, CustomTestDataProvider):
    post_text_area = (By.XPATH, "//div[@id='create-post']//textarea[@id='comment']")
    image_upload_field = (By.XPATH, "//input[@id='imt-upld']")
    post_btn = (By.XPATH, "//button[normalize-space()='Post']")

    def __init__(self, driver):
        super().__init__(driver)
        self.login_page = LoginPage(self.driver)

    def type_text_on_field(self, text):
        self.type_text(self.post_text_area, text)

    def click_post_button(self):
        try:
            self.click_on_web_element_with_actions_class(self.post_btn)
            return True
        except Exception as e:
            logger.error("Failed to click on post button with exception: ", e)
            return AssertionError

    def verify_post_text_on_timeline(self, text):
        self.wait_until_visible((By.XPATH, "//*[contains(text(), '" + text + "')]"))

    def post_text_successfully(self):

        try:
            step = 0

            random_sentence = self.random_sentence()

            self.login_page.login()
            step += 1
            logger.info(str(step) + ": Typed text on the field")

            self.type_text_on_field(random_sentence)
            step += 1
            logger.info(str(step) + ": Typed text on the field")

            self.click_post_button()
            step += 1
            logger.info(str(step) + ": Clicked on post button")

            self.verify_post_text_on_timeline(random_sentence)
            step += 1
            logger.info(str(step) + ": Post text verified on timeline")

            return True

        except Exception as e:
            logger.error("Couldn't post text: ", e)
            return False

    # login with invalid credentials
    def login_with_invalid_credentials_failed(self):
        try:
            step = 0

            self.click_login_link()
            step += 1
            logger.info(str(step) + ": Clicked on login link")

            self.type_email(self.get_new_email())
            step += 1
            logger.info(str(step) + ": Typed email")

            self.type_password(self.get_14_digit_hard_password())
            step += 1
            logger.info(str(step) + ": Typed password")

            self.click_login_button()
            step += 1
            logger.info(str(step) + ": Clicked on login button")

            self.verify_invalid_credentials_msg()
            step += 1
            logger.info(str(step) + ": Login failed with invalid credentials")

            return True

        except Exception as e:
            logger.error("Login failed with exception: ", e)
            return False
