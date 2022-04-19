
from selenium.webdriver.common.by import By

from data_provider.test_data_provider import CustomTestDataProvider
from page_objects.base_page import BasePage
from helper.driver_actions import DriverActions
from helper.driver_waits import DriverWaits
from utils.logger import CustomLogger

logger = CustomLogger("login_page_log").get_logger()


class LoginPage(BasePage, DriverActions, DriverWaits, CustomTestDataProvider):
    LOGIN_LINK = (By.XPATH, "//a[normalize-space()='LogIn']")
    EMAIL_FIELD = (By.XPATH, "//input[@placeholder='YOUR EMAIL *']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='LOGIN']")
    MESSAGES_LINK = (By.XPATH, "//div[contains(text(),'Messages')]")
    INVALID_CREDENTIALS_MSG = (By.XPATH, "//*[contains(text(),'Invalid credentials')]")

    def __init__(self, driver):
        super().__init__(driver)

    def type_email(self, email):
        self.type_text(self.EMAIL_FIELD, email)

    def type_password(self, password):
        self.type_text(self.PASSWORD_FIELD, password)

    def click_login_button(self):
        self.click_on_web_element_with_actions_class(self.LOGIN_BUTTON)

    def click_login_link(self):
        self.click_on_web_element_with_actions_class(self.LOGIN_LINK)

    def verify_invalid_credentials_msg(self):
        try:
            self.wait_until_visible(self.INVALID_CREDENTIALS_MSG, 20)
            return True
        except Exception as e:
            logger.error("Invalid credentials message not found with exception: ", e)

    def check_message_link_after_login(self):
        try:
            self.wait_until_visible(self.MESSAGES_LINK, 20)
            return True
        except Exception as e:
            logger.error("Message link not found with exception: ", e)
            raise AssertionError

    def login(self, email, password):
        try:
            step = 0

            self.click_login_link()
            step += 1
            logger.info(str(step) + ": Clicked on login link")

            self.type_email(email)
            step += 1
            logger.info(str(step) + ": Typed email")

            self.type_password(password)
            step += 1
            logger.info(str(step) + ": Typed password")

            self.click_login_button()
            step += 1
            logger.info(str(step) + ": Clicked on login button")

            self.check_message_link_after_login()
            step += 1
            logger.info(str(step) + ": Logged in successfully")

            return True

        except Exception as e:
            logger.error("Login failed with exception: ", e)
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
