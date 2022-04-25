import random
import time

from selenium.webdriver.common.by import By

from data_provider.test_data_provider import CustomTestDataProvider
from page_objects.base_page import BasePage
from helper.driver_actions import DriverActions
from helper.driver_waits import DriverWaits
from page_objects.login_page import LoginPage
from utils.logger import CustomLogger

logger = CustomLogger("marketplace").get_logger()


class MarketPlacePage(BasePage, DriverActions, DriverWaits, CustomTestDataProvider):
    # Marketplace Locators
    marketplace_link = (By.XPATH, "//a[@class='icon-holder'][normalize-space()='IndyMarket']")
    search_input_field = (By.XPATH, "//input[@placeholder='Search IndyMarket']")
    search_category = (By.XPATH, "//select[@id='category']")
    search_sub_category = (By.XPATH, "//select[@id='subCategory']")
    search_btn = (By.XPATH, "//button[normalize-space()='Search']")
    welcome_msg = (By.XPATH, "//p[normalize-space()='Welcome to IndyMarket']")
    view_all_album_link = (By.XPATH, "//a[@href='/indymarket/album?indymarket=all']")
    view_all_audio_link = (By.XPATH, "//a[@href='/indymarket/audio?indymarket=all']")
    view_all_video_link = (By.XPATH, "//a[@href='/indymarket/video?indymarket=all']")
    view_all_paint_link = (By.XPATH, "//a[@href='/indymarket/picture?indymarket=all']")
    albums = (By.XPATH, "//h4[normalize-space()='Album(s)']")
    audios = (By.XPATH, "//h4[normalize-space()='Audio(s)']")
    videos = (By.XPATH, "//h4[normalize-space()='Video(s)']")
    pictures = (By.XPATH, "//h4[normalize-space()='Picture(s)']")
    back_to_marketplace_btn = (By.XPATH, "//button[normalize-space()='Back To IndyMarket']")
    album_elems = (By.XPATH, "(//*[contains(text(), 'Top Albums On IndyBuild')]/ancestor::div/child::div/child::div)[1]/child::div/div")

    add_to_cart_btn = (By.XPATH, "//button[normalize-space()='ADD TO CART']")

    # End Locators

    def __init__(self, driver):
        super().__init__(driver)
        self.login_page = LoginPage(self.driver)

    def click_back_to_marketplace_btn(self):
        time.sleep(1)
        self.click_on_web_element_with_actions_class(self.back_to_marketplace_btn)
        time.sleep(1)
        assert self.wait_until_visible(self.welcome_msg) is True, "Welcome message is not visible"

    def go_to_marketplace(self):
        try:
            time.sleep(5)
            self.click_on_web_element_with_actions_class(self.marketplace_link)
            logger.info("Marketplace link clicked")
        except Exception as e:
            logger.error("Marketplace link not clicked, error ", e)

    def click_view_all_albums_link(self):
        try:
            self.click_on_web_element_with_actions_class(self.view_all_album_link)
            logger.info("View all album link clicked")
            time.sleep(3)
            assert self.wait_until_visible(self.albums) is True
            logger.info("Albums displayed")
        except Exception as e:
            logger.error("View all album link not clicked, error: ", e)

    def click_view_all_audios_link(self):
        try:
            time.sleep(1)
            self.click_on_web_element_with_actions_class(self.view_all_audio_link)
            logger.info("View all audio link clicked")
            assert self.wait_until_visible(self.audios) is True
            logger.info("Audios displayed")
        except Exception as e:
            logger.error("View all audio link not clicked, error: ", e)

    def click_view_all_videos_link(self):
        try:
            time.sleep(2)
            self.click_on_web_element_with_actions_class(self.view_all_video_link)
            logger.info("View all video link clicked")
            assert self.wait_until_visible(self.videos) is True
            logger.info("Videos displayed")
        except Exception as e:
            logger.error("View all video link not clicked, error: ", e)

    def click_view_all_pictures_link(self):
        try:
            self.click_on_web_element_with_actions_class(self.view_all_paint_link)
            logger.info("View all pictures link clicked")
            assert self.wait_until_visible(self.pictures) is True
            logger.info("Pictures displayed")
        except Exception as e:
            logger.error("View all pictures link not clicked, error: ", e)

    def check_a_random_item_from_album(self):
        elements = self.find_elements(self.album_elems)
        random_elem = random.choice(elements)
        self.click_on_web_element_with_actions_class(random_elem)
        assert self.wait_until_visible(self.add_to_cart_btn) is True, "Add to cart button not displayed"

    def view_all_link_check(self):
        try:
            step = 0

            self.login_page.login()
            step += 1
            logger.info("Login successful")

            self.go_to_marketplace()
            step += 1
            logger.info("Marketplace link clicked")

            self.wait_until_visible(self.welcome_msg)
            step += 1
            logger.info("Welcome message displayed")

            self.click_view_all_albums_link()
            step += 1
            logger.info(str(step), " albums displayed")
            self.click_back_to_marketplace_btn()

            self.click_view_all_audios_link()
            step += 1
            logger.info(str(step), " audios displayed")
            self.click_back_to_marketplace_btn()

            self.click_view_all_videos_link()
            step += 1
            logger.info(str(step), " videos displayed")
            self.click_back_to_marketplace_btn()

            self.click_view_all_pictures_link()
            step += 1
            logger.info(str(step), " pictures displayed")
            self.click_back_to_marketplace_btn()

            logger.info("All links clicked")

            return True

        except Exception as e:
            logger.error("View all link not clicked, error: ", e)
            return False

    def check_item_detail(self):
        try:
            step = 0

            self.login_page.login()
            step += 1
            logger.info("Login successful")

            self.go_to_marketplace()
            step += 1
            logger.info("Marketplace link clicked")

            self.wait_until_visible(self.welcome_msg)
            step += 1
            logger.info("Welcome message displayed")

            self.check_a_random_item_from_album()
            step += 1
            logger.info("Random item from album clicked")

            return True

        except Exception as e:
            logger.error("Item detail not checked, error: ", e)
            return False
