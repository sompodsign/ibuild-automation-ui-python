import allure

from page_objects.base_page import BasePage
from helper.driver_actions import DriverActions
from helper.driver_waits import DriverWaits
from locators.locators import HomePageLocators
from utils.logger import CustomLogger

logger = CustomLogger("home_page_test").get_logger()


class HomePage(BasePage, DriverActions, DriverWaits):

    def __init__(self, driver):
        self.home_page_locator = HomePageLocators
        super().__init__(driver)

    @allure.step("Checking the favicon of the page if visible")
    def check_favicon(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.FAVICON) is True
            logger.info("Favicon is visible")
            return True
        except AssertionError:
            logger.error("Favicon is not visible")
            raise AssertionError

    @allure.step("Checking the logo is visible properly")
    def check_logo(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.LOGO) is True
            logger.info("Logo is visible on the page")
            return True
        except Exception as e:
            logger.error(f"Logo is not visible on the page: {e}")
            raise AssertionError

    @allure.step("Checking footer menu items")
    def check_footer_menu_items(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.FOOTER_MENU_ITEMS) is True
            logger.info("Footer menu items are visible")
            return True
        except AssertionError:
            logger.error("Footer menu items are not visible")
            raise AssertionError

    @allure.step("Check login button")
    def check_login_button(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.LOGIN_LINK) is True
            logger.info("Login button is visible")
            return True
        except AssertionError:
            logger.error("Login button is not visible")
            raise AssertionError

    @allure.step("Checking if the 'Sign Up' button is visible")
    def check_sign_up_button(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.SIGNUP_LINK) is True
            logger.info("Sign Up button is visible")
            return True
        except AssertionError:
            logger.error("Sign Up button is not visible")
            raise AssertionError

    @allure.step("Checking if the 'Join Today' button is visible on the home page")
    def check_join_today_button(self):
        try:
            assert self.wait_until_visible(self.home_page_locator.JOIN_TODAY_BTN) is True
            logger.info("Join Today button is visible")
            return True
        except AssertionError:
            logger.error("Join Today button is not visible")
            raise AssertionError

    def check_home_page_elements(self):
        """
        This method checks if all the elements on the home page are visible
        :return:
        """
        try:
            self.check_logo(),
            self.check_login_button(),
            self.check_sign_up_button(),
            self.check_join_today_button(),
            self.check_footer_menu_items(),
            return True
        except AssertionError:
            logger.error("Some Home page elements are not visible")
            return False

