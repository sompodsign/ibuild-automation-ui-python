from browser_utility.browser import Browser
from helper.driver_actions import DriverActions
from helper.driver_waits import DriverWaits


class DriverUtils:

    @staticmethod
    def get_driver_actions_object():
        return DriverActions(Browser().get_web_driver())

    @staticmethod
    def get_driver_waits_object():
        return DriverWaits(Browser().get_web_driver())


driver_utils = DriverUtils()
