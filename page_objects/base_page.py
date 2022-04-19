import logging

from application_settings.application_settings import ApplicationSettings


class BasePage(object):
    """
    Base class to initialize the base page that will be called from all pages
    """
    application_settings = ApplicationSettings()

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    def get_page_title(self):
        return self.driver.title

    def get_page_url(self):
        return self.driver.current_url

    def get_page_source(self):
        return self.driver.page_source

