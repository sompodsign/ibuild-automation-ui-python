import allure

from page_objects.market_place_page import MarketPlacePage
from tests.base_test import BaseTest
from application_settings.application_settings import ApplicationSettings


class MarketPlacePageTest(BaseTest):
    application_settings = ApplicationSettings()
    data = application_settings.get_test_data_from_excel("login", "login_data")

    @allure.title("MarketPlacePage - Sanity Test")
    @allure.description("Checking if a user can visit view all links on marketplace page")
    def test_01_marketplace_view_all_links_check(self):
        timeline_page = MarketPlacePage(self.driver)
        print("Starting to test marketplace page")
        assert timeline_page.view_all_link_check() is True, "views all links failed"

    @allure.title("Marketplace Page - Sanity Test")
    @allure.description("Chekcking if a user can see all the details for a item")
    def test_02_detail_check_for_a_item(self):
        timeline_page = MarketPlacePage(self.driver)
        print("Starting to detail page check")
        assert timeline_page.check_item_detail() is True, "detail checking failed"
    #
    # @allure.title("Timeline Page - Sanity Test")
    # @allure.description("Checking if a user can post video on timeline")
    # def test_03_post_video_successfully(self):
    #     timeline_page = TimeLinePage(self.driver)
    #     print("Starting to test video sharing functionality")
    #     assert timeline_page.post_video_successfully() is True, "Video posting failed"
    #
    # @allure.title("Timeline Page - Sanity Test")
    # @allure.description("Checking if a user can post audio on timeline")
    # def test_04_post_audio_successfully(self):
    #     timeline_page = TimeLinePage(self.driver)
    #     print("Starting to test audio sharing functionality")
    #     assert timeline_page.post_audio_successfully() is True, "Audio posting failed"
    #
    # @allure.title("Timeline Page - Sanity Test")
    # @allure.description("Checking if a user can search for another user on timeline")
    # def test_05_search_functionality(self):
    #     timeline_page = TimeLinePage(self.driver)
    #     print("Starting to test search functionality")
    #     assert timeline_page.search_user_successfully() is True, "Searching failed"
    #
    # @allure.title("Timeline Page - Sanity Test")
    # @allure.description("Checking if a user can seamlessly browse upcoming features")
    # def test_06_upcoming_events(self):
    #     timeline_page = TimeLinePage(self.driver)
    #     print("Starting to test Upcoming Events")
    #     assert timeline_page.check_upcoming_events_functionalities_on_timeline() is True, "Something went wrong " \
    #                                                                                       "on upcoming events"
    #
    # @allure.title("Timeline Page - Sanity Test")
    # @allure.description("Checking if a user can seamlessly browse build connection")
    # def test_07_build_connection_features(self):
    #     timeline_page = TimeLinePage(self.driver)
    #     print("Starting to test Build Connections")
    #     assert timeline_page.check_build_connections_on_timeline() is True, "Something went wrong " \
    #                                                                         "on Build connections"
    #
    # @allure.title("Timeline Page - Sanity Test")
    # @allure.description("Checking if a user can browse left sidebar links seamlessly")
    # def test_08_left_sidebar_navigation(self):
    #     timeline_page = TimeLinePage(self.driver)
    #     print("Starting to left sidebar navigation")
    #     assert timeline_page.check_left_sidebar_navigation() is True, "Something went wrong " \
    #                                                                   "on left sidebar navigation"
