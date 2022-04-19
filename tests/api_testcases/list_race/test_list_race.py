import allure
from application_settings.api_application_settings import CustomTestApplicationSettingsProvider
from test_data.api_test_data.game_api_data import GameData
from utils.logger import CustomLogger

logger = CustomLogger('api_test').get_logger()


class TestListRace(GameData):

    api = CustomTestApplicationSettingsProvider('/game/api/race')

    @allure.step('Successful list races')
    def test_list_race(self):
        result = self.api.get_request()
        try:
            assert result['status_code'] == 200
            assert isinstance(result['response']['races'], list)
            logger.info("Race list retrieved successfully")
        except Exception as e:
            logger.error(f"Failed retrieving race list {e}")
            raise AssertionError

    @allure.step('Failed list race with post request')
    def test_list_race_with_post_request(self):
        result = self.api.post_request({"data": "testdata"})
        try:
            assert result['status_code'] == 400
            assert result['response']['message'] == ['event should not be empty', 'location should not be empty', 'entranceFee should not be empty', 'eventType should not be empty', 'raceTime should not be empty']
            logger.info("Failed races list retrieving with post request")
        except Exception as e:
            logger.error(f"Success retrieving race list with post request {e}")
            raise AssertionError

    @allure.step('Failed list race with put request')
    def test_list_race_with_put_request(self):
        result = self.api.put_request({"data": "testdata"})
        try:
            assert result['status_code'] == 404
            assert result['response']['message'] == 'Cannot PUT /game/api/race'
            logger.info("Failed races list retrieving with put request")
        except Exception as e:
            logger.error(f"Success retrieving race list with put request {e}")
            raise AssertionError

    @allure.step('Failed list race with delete request')
    def test_list_race_with_delete_request(self):
        result = self.api.delete_request({"data": "testdata"})
        try:
            assert result['status_code'] == 404
            assert result['response']['message'] == 'Cannot DELETE /game/api/race'
            logger.info("Failed races list retrieving with delete request")
        except Exception as e:
            logger.error(f"Success retrieving race list with delete request {e}")
            raise AssertionError
