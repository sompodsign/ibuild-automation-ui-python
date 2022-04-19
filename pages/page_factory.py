from helper.driver_actions import DriverActions
from helper.driver_waits import DriverWaits
from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage


def get_login_page(driver):
    return LoginPage(driver)


def get_home_page(driver):
    return HomePage(driver)


class PageFactory:
    # def __init__(self, driver):
    #     self.driver = driver

    pass

    # def get_driver_actions_object(self):
    #     return DriverActions(self.driver)
    #
    # def get_driver_waits_object(self):
    #     return DriverWaits(self.driver)


