import allure
import pytest

from application_settings.api_application_settings import CustomTestApplicationSettingsProvider
from test_data.api_test_data.game_api_data import GameData
from utils.logger import CustomLogger

logger = CustomLogger('api_test').get_logger()


@pytest.mark.one
class TestSaveRace(GameData):
    api = CustomTestApplicationSettingsProvider('/game/api/race')

    @allure.step('Successful save race')
    @pytest.mark.skip
    def test_save_race(self):
        result = self.api.post_request(self.get_new_race_data())
        try:
            assert result['status_code'] == 201
            assert result['response']['message'] == 'Race saved successfully'
            logger.info("Race saved successfully with valid data")
        except Exception as e:
            logger.error(f"Race Saving failed {e}")
            raise AssertionError

    @allure.step('Failed saving race with empty event name')
    def test_save_race_with_empty_event_name(self):
        result = self.api.post_request(self.get_new_race_data_without_event())
        try:
            assert result['status_code'] == 400
            assert result['response']['message'] == ['event should not be empty']
            logger.info("Race not saved without event name")
        except Exception as e:
            logger.error(f"Race Saving failed without event name{e}")
            raise AssertionError

    @allure.step('Failed saving race with empty location')
    def test_save_race_with_empty_location(self):
        result = self.api.post_request(self.get_new_race_data_without_location())
        try:
            assert result['status_code'] == 400
            assert result['response']['message'] == ['location should not be empty']
            logger.info("Race not saved without location ")
        except Exception as e:
            logger.error(f"Race Saving failed without location {e}")
            raise AssertionError

    @allure.step('Failed saving race with empty entrance fee')
    def test_save_race_with_empty_entrance_fee(self):
        result = self.api.post_request(self.get_new_race_data_without_entrance_fee())
        try:
            assert result['status_code'] == 400
            assert result['response']['message'] == ['entranceFee should not be empty']
            logger.info("Race not saved without Entrance Fee ")
        except Exception as e:
            logger.error(f"Race Saving failed without Entrance Fee {e}")
            raise AssertionError

    @allure.step('Failed saving race with empty event type')
    def test_save_race_with_empty_event_type(self):
        result = self.api.post_request(self.get_new_race_data_without_event_type())
        try:
            assert result['status_code'] == 400
            assert result['response']['message'] == ['eventType should not be empty']
            logger.info("Race not saved without eventType")
        except Exception as e:
            logger.error(f"Race Saving failed without eventType {e}")
            raise AssertionError

    @allure.step('Failed saving race with empty race time')
    def test_save_race_with_empty_race_time(self):
        result = self.api.post_request(self.get_new_race_data_without_race_time())
        try:
            assert result['status_code'] == 400
            assert result['response']['message'] == ['raceTime should not be empty']
            logger.info("Race not saved without race time")
        except Exception as e:
            logger.error(f"Race Saving failed without race time {e}")
            raise AssertionError

    @allure.step('Failed saving race with put request')
    def test_save_race_with_put_request(self):
        result = self.api.put_request(self.get_new_race_data())
        try:
            assert result['status_code'] == 404
            logger.info("Race not saved with put request")
        except Exception as e:
            logger.error(f"Race Saving failed with put request {e}")
            raise AssertionError

    @allure.step('Failed saving race with delete request')
    def test_save_race_with_delete_request(self):
        result = self.api.delete_request()
        try:
            assert result['status_code'] == 404
            logger.info("Race not saved with delete request")
        except Exception as e:
            logger.error(f"Race Saving failed with delete request {e}")
            raise AssertionError
