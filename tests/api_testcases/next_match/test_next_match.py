import allure
from application_settings.api_application_settings import CustomTestApplicationSettingsProvider

from utils.logger import CustomLogger
logger = CustomLogger('api_test').get_logger()


class TestNextMatch:

    api = CustomTestApplicationSettingsProvider('/game/api/match')

    @allure.step('Successful next match retrieve')
    def test_next_match(self):
        result = self.api.get_request()
        status_code = result['status_code']
        try:
            assert status_code == 200
            assert isinstance(result['response']['matchId'], str)
            logger.info('Next match retrieved successfully')
        except AssertionError as e:
            logger.error(f"Next match not retrieved something is wrong: {e}")
            assert AssertionError

    @allure.step('Failed retrieve next match with post request')
    def test_next_match_post(self):
        result = self.api.post_request()
        status_code = result['status_code']
        try:
            assert status_code == 400
            assert result['response']['message'] == ['matchId should not be empty', 'dogs must be an array', 'dogs should not be empty']
            logger.info('Next match not retrieved successfully with post request')
        except AssertionError as e:
            logger.error(f"Next match not retrieved successfully with post request: {e}")
            assert AssertionError

    @allure.step('Failed retrieve next match with put reqeust')
    def test_next_match_put(self):
        result = self.api.put_request()
        status_code = result['status_code']
        try:
            assert status_code == 404
            assert result['response']['message'] == 'Cannot PUT /game/api/match'
            logger.info('Next match not retrieved successfully with put request')
        except AssertionError as e:
            logger.error(f"Next match not retrieved successfully with put request: {e}")
            assert AssertionError

    @allure.step('Failed retrieve next match with delete request')
    def test_next_match_delete(self):
        result = self.api.delete_request()
        status_code = result['status_code']
        try:
            assert status_code == 404
            assert result['response']['message'] == 'Cannot DELETE /game/api/match'
            logger.info('Next match not retrieved successfully with delete request')
        except AssertionError as e:
            logger.error(f"Next match not retrieved successfully with delete request: {e}")
            assert AssertionError
