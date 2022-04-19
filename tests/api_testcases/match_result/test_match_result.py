import allure
import pytest
from application_settings.api_application_settings import CustomTestApplicationSettingsProvider
from test_data.api_test_data.game_api_data import GameData
from utils.logger import CustomLogger

logger = CustomLogger('api_test').get_logger()


@pytest.mark.skip
class TestMatchResult(GameData):
    match_api = CustomTestApplicationSettingsProvider('/game/api/match')
    next_match_api = CustomTestApplicationSettingsProvider('/game/api/match')

    @allure.step('Successful retrieve match result')
    def test_match_result(self):
        next_match_result = self.next_match_api.get_request()
        random_match_id = next_match_result['response']
        # random_dog = next_match_result['response']['dogs'][0]['id']
        # payload = {
        #     "matchId": random_match_id,
        #     "dogs": [random_dog]
        # }
        # result = self.match_api.post_request(payload)
        # try:
        #     assert result['status_code'] == 201
        #     assert result['response']['message'] == 'Result Send successfully'
        #     assert result['response']['success'] is True
        #     logger.info("Successful retrieve match result")
        # except AssertionError as e:
        #     logger.error(f"Failed to retrieve match result: {e}")
        #     raise AssertionError

    @allure.step('Failed retrieve match result with invalid match id')
    def test_match_result_with_invalid_match_id(self):
        result = self.match_api.post_request(self.get_payload_with_empty_match_id())
        try:
            assert result['status_code'] == 400
            assert result['response']['message'] == ['matchId should not be empty']
            logger.info("Failed retrieve match result with invalid match id")
        except AssertionError as e:
            logger.error(f"Successful to retrieve match result with empty match id: {e}")
            raise AssertionError

    @allure.step('Failed retrieve match result with invalid dog id')
    def test_match_result_with_invalid_dog_id(self):
        result = self.match_api.post_request(self.get_payload_with_empty_dogs_id())
        try:
            assert result['status_code'] == 400
            # assert result['response']['message'] == ['dogs should not be empty']
            logger.info("Failed retrieve match result with empty dog id")
        except AssertionError as e:
            logger.error(f"Successful to retrieve match result with invalid dog id: {e}")
            raise AssertionError
