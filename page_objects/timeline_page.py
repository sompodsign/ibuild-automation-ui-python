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
    # Start Locators
    post_text_area = (By.XPATH, "//div[@id='create-post']//textarea[@id='comment']")
    image_upload_field = (By.XPATH, "//input[@id='imt-upld']")
    post_btn = (By.XPATH, "//button[normalize-space()='Post']")
    upload_btn = (By.XPATH, "//button[normalize-space()='Upload']")
    few_seconds_ago = (By.XPATH, "//*[contains(text(),'a few seconds ago')]")
    video_upload_field = (By.XPATH, "//input[@id='attahcment']")
    audio_upload_field = (By.XPATH, "//input[@id='sound']")
    search_input_field = (By.XPATH, "//input[@placeholder='Search IndyBuild']")
    search_result = (By.XPATH, "//*[contains(text(),'Unidevgo_qa')]")
    upcoming_see_all_link = (By.XPATH, "//a[@class='right-side-links']")
    # Events page
    buy_tickets_btn = (By.XPATH, "//button[@type='button'][normalize-space()='Buy Tickets']")
    events_page_header = (By.XPATH, "//h4[normalize-space()='Events That Match Your Interests.']")
    purchase_tickets_header = (By.XPATH, "//h2[normalize-space()='Purchase Tickets']")
    close_modal = (By.XPATH, "//img[@data-dismiss='modal']")
    upcoming_events_details_btn_specific = (By.XPATH, "(//button[@type='button'][normalize-space()='Details'])[1]")
    upcoming_events_details_btn = (By.XPATH, "//button[@type='button'][normalize-space()='Details']")
    upcoming_events_header_on_timeline = (By.XPATH, "//*[contains(text(), 'Upcoming Events')]")
    evnet_header_modal = (By.XPATH, "//h2[normalize-space()='Event']")
    # Build connections
    build_connections_header = (By.XPATH, "//h4[contains(.,'Build Connections')]")
    connect_link = (By.XPATH, "//h4[contains(.,'Build Connections')]//a")
    community_header = (By.XPATH, "//*[.='Build your community now!']")
    invite_google_contacts = (By.XPATH, "//a[normalize-space()='Invite Google Contacts']")
    invite_what_app_contacts = (By.XPATH, "//a[normalize-space()='Invite Whatsapp Contacts']")
    back_btn_on_community = (By.XPATH, "//button[@id='nextBtn']")

    # Left sidebar
    artist_link = (By.XPATH, "//div[@class='post-profile pro-user-section']//app-profile-image-widget")
    earnings_link = (By.XPATH, "//span[normalize-space()='EARNINGS']")
    my_activity_header = (By.XPATH, "//h3[normalize-space()='My Activity']")
    messages_link = (By.XPATH, "//div[contains(text(),'Messages')]")
    message_search_field = (By.XPATH, "//input[@placeholder='People, Professionals, Messages']")
    interests_link = (By.XPATH, "//div[contains(text(),'Interests')]")
    my_library_link = (By.XPATH, "//div[contains(text(),'My Library')]")
    my_store_link = (By.XPATH, "//div[contains(text(),'My Store')]")
    welcome_store_msg = (By.XPATH, "//p[.='Welcome to Your Store']")
    my_events_link = (By.XPATH, "//div[contains(text(),'My Events')]")
    dashboard_link = (By.XPATH, "//div[contains(text(),'Dashboard')]")

    # End Locators

    def __init__(self, driver):
        super().__init__(driver)
        self.login_page = LoginPage(self.driver)

    def back_to_time_line(self):
        self.go_to("http://indybuildpro.com/talent/home")
        time.sleep(5)

    def type_text_on_field(self, text):
        self.type_text(self.post_text_area, text)

    def click_upload_btn(self):
        try:
            self.wait_until_visible(self.upload_btn, 10)
            time.sleep(6)
            self.click_on_web_element_with_actions_class(self.upload_btn)
            return True
        except Exception as e:
            logger.error("Couldn't click on upload button: ", e)
            raise AssertionError

    def click_post_button(self):
        try:
            self.wait_until_visible(self.post_btn, 10)
            time.sleep(5)
            self.click_on_web_element_with_actions_class(self.post_btn)
            return True
        except Exception as e:
            logger.error("Failed to click on post button with exception: ", e)
            return AssertionError

    def verify_post_text_on_timeline(self, text):
        self.wait_until_visible((By.XPATH, "//*[contains(text(), '" + text + "')]"))

    def upload_image_on_timeline(self, image_name):
        try:
            self.upload_image(self.image_upload_field, image_name)
            return True
        except Exception as e:
            logger.error("Couldn't upload image: ", e)
            raise AssertionError

    def upload_video_on_timeline(self, video_file_name):
        try:
            self.upload_video(self.video_upload_field, video_file_name)
            return True
        except Exception as e:
            logger.error("Couldn't upload video: ", e)
            raise AssertionError

    def upload_audio_on_timeline(self, audio_file_name):
        try:
            self.upload_audio(self.audio_upload_field, audio_file_name)
            return True
        except Exception as e:
            logger.error("Couldn't upload audio: ", e)
            raise AssertionError

    def upcoming_events_details_btn_check(self):
        self.wait_until_visible(self.upcoming_events_details_btn_specific, 10)
        try:
            buttons = self.find_elements(*self.upcoming_events_details_btn)
            for button in buttons:
                button.click()
                self.implicit_wait(2)
                self.wait_until_visible(self.evnet_header_modal, 10)
                self.click_on_web_element_with_actions_class(self.close_modal)
            return True
        except Exception as e:
            logger.error("Couldn't click on upcoming events details button: ", e)
            raise False

    def click_artists_link(self):
        time.sleep(5)
        self.click_on_web_element_with_actions_class(self.artist_link)  # click on artist link
        assert "profile" in self.get_page_url()

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

    def post_image_successfully(self):
        try:
            step = 0

            self.login_page.login()
            step += 1
            logger.info(str(step) + ": Logged In")

            self.upload_image_on_timeline("test-image-1.jpg")
            step += 1
            logger.info(str(step) + ": Uploaded image on timeline")

            self.click_upload_btn()
            step += 1
            logger.info(str(step) + ": Clicked on upload button")

            self.click_post_button()
            step += 1
            logger.info(str(step) + ": Clicked on post button")

            return self.wait_until_visible(self.few_seconds_ago, 10)

        except Exception as e:
            logger.error("Couldn't post image: ", e)
            return False

    def post_video_successfully(self):
        try:
            step = 0

            self.login_page.login()
            step += 1
            logger.info(str(step) + ": Logged In")

            self.upload_video_on_timeline("test-video-1.mp4")
            step += 1
            logger.info(str(step) + ": Uploaded video on timeline")

            self.click_post_button()
            step += 1
            logger.info(str(step) + ": Clicked on post button")

            return self.wait_until_visible(self.few_seconds_ago, 10)

        except Exception as e:
            logger.error("Couldn't post image: ", e)
            return False

    def post_audio_successfully(self):
        try:
            step = 0

            self.login_page.login()
            step += 1
            logger.info(str(step) + ": Logged In")

            self.upload_audio_on_timeline("test-audio-1.mp3")
            step += 1
            logger.info(str(step) + ": Uploaded audio on timeline")

            self.click_post_button()
            step += 1
            logger.info(str(step) + ": Clicked on post button")

            return self.wait_until_visible(self.few_seconds_ago, 10)

        except Exception as e:
            logger.error("Couldn't post audio: ", e)
            return False

    def search_user_successfully(self):
        try:
            step = 0

            self.login_page.login()
            step += 1
            logger.info(str(step) + ": Logged In")

            self.type_text(self.search_input_field, "unidev")
            step += 1
            logger.info(str(step) + ": Searched user on timeline")

            self.wait_until_visible(self.search_result, 10)

            self.click_on_web_element_with_actions_class(self.search_result)
            step += 1
            logger.info(str(step) + ": Clicked on search result")

            return "profile" in self.get_page_url()

        except Exception as e:
            logger.error("Couldn't search user: ", e)
            return False

    def check_upcoming_events_functionalities_on_timeline(self):
        try:
            step = 0
            self.login_page.login()
            step += 1
            logger.info(str(step) + ": Logged In")

            assert self.wait_until_visible(self.upcoming_events_header_on_timeline, 10)
            step += 1
            logger.info(str(step) + ": Upcoming events header is visible")

            return self.upcoming_events_details_btn_check()

        except Exception as e:
            logger.error("Couldn't check upcoming events functionality on timeline: ", e)
            return False

    def check_build_connections_on_timeline(self):
        try:
            step = 0
            self.login_page.login()
            step += 1
            logger.info(str(step) + ": Logged In")

            assert self.wait_until_visible(self.build_connections_header, 10)
            step += 1
            logger.info(str(step) + ": Build connections header is visible on timeline")

            self.wait_until_visible(self.connect_link, 10)
            assert self.click_on_web_element_with_actions_class(self.connect_link) is True
            step += 1
            logger.info(str(step) + ": Clicked on connect link")

            self.wait_until_visible(self.community_header, 10)
            step += 1
            logger.info(str(step) + ": Community header is visible on connect page")

            self.wait_until_visible(self.invite_google_contacts, 10)
            step += 1
            logger.info(str(step) + ": Invite google contacts button is visible on connect page")

            self.wait_until_visible(self.invite_what_app_contacts, 10)
            step += 1
            logger.info(str(step) + ": Invite what app contacts button is visible on connect page")

            self.click_on_web_element_with_actions_class(self.back_btn_on_community)
            step += 1
            logger.info(str(step) + ": Clicked on back button on community page")

            return self.wait_until_visible(self.post_text_area, 10)

        except Exception as e:
            logger.error("Couldn't check build connections on timeline: ", e)
            return False

    def check_left_sidebar_navigation(self):
        try:
            step = 0

            self.login_page.login()
            step += 1
            logger.info(str(step) + ": Logged In")

            # self.wait_until_visible(self.artist_link, 10)
            # time.sleep(5)
            # self.click_on_web_element_with_actions_class(self.artist_link)
            # self.wait_until_visible((By.XPATH, "//div[@class='artist-name']"), 10)
            #

            self.click_artists_link()
            step += 1
            logger.info(str(step) + ": Clicked on artists link")
            self.back_to_time_line()

            self.click_on_web_element_with_actions_class(self.earnings_link)
            assert self.wait_until_visible(self.my_activity_header, 10) is True
            self.back_to_time_line()
            step += 1
            logger.info(str(step) + ": Clicked on earnings link and activity header is visible")

            self.click_on_web_element_with_actions_class(self.messages_link)
            assert self.wait_until_visible(self.message_search_field, 10) is True
            step += 1
            logger.info(str(step) + ": Clicked on messages link and message search field is visible")
            self.back_to_time_line()

            self.click_on_web_element_with_actions_class(self.interests_link)
            assert "interest" in self.get_page_url()
            self.back_to_time_line()
            step += 1
            logger.info(str(step) + ": Clicked on interests link and interests page is opened")

            self.click_on_web_element_with_actions_class(self.my_library_link)
            time.sleep(2)
            assert "library" in self.get_page_url()
            step += 1
            logger.info(str(step) + ": Clicked on my library link and library page is opened")
            self.back_to_time_line()

            self.click_on_web_element_with_actions_class(self.my_store_link)
            assert self.wait_until_visible(self.welcome_store_msg, 10) is True
            step += 1
            logger.info(str(step) + ": Clicked on my store link and welcome store message is visible")
            self.back_to_time_line()

            self.click_on_web_element_with_actions_class(self.my_events_link)
            time.sleep(2)
            assert "myevents" in self.get_page_url()
            step += 1
            logger.info(str(step) + ": Clicked on my events link and my events page is opened")
            self.back_to_time_line()

            self.click_on_web_element_with_actions_class(self.dashboard_link)
            assert self.wait_until_visible(self.my_activity_header, 10) is True
            step += 1
            logger.info(str(step) + ": Clicked on dashboard link and activity header is visible")
            self.back_to_time_line()

            return True

        except Exception as e:
            logger.error("Couldn't check left sidebar navigation: ", e)
            return False
