import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class DriverWaits:
    """
    This class contains methods to wait for elements to appear on the page.
    """

    def __init__(self, driver):
        self.driver = driver

    def get_wait(self, wait=10):
        return WebDriverWait(self.driver, wait)

    def explicit_wait(self, element, wait_time):
        """
        Wait until element is visible
        :param element:
        :param wait_time:
        :return:
        """
        try:
            self.get_wait(wait_time).until(EC.presence_of_element_located(element))
        except Exception as e:
            print(e, "not found")

    def wait_until_visible(self, element, wait_time=5):
        """
        Wait until element is visible
        :param wait_time:
        :param element:
        :return:
        """
        time.sleep(0.3)
        try:
            self.get_wait(wait_time).until(EC.visibility_of_element_located(element))
            return True
        except Exception as e:
            print(e, "not found", element)
            return False

    def wait_till_completely_loaded(self, wait_time):
        """
        Wait until the page is completely loaded
        :param wait_time:
        :return: boolean
        """
        try:
            js = "return document.readyState"
            self.get_wait(wait_time).until(lambda driver: driver.execute_script(js) == "complete")
            return True
        except Exception as e:
            print("Something went wrong: ", e)
            return False

    @staticmethod
    def implicit_wait(wait_time):
        time.sleep(wait_time)
