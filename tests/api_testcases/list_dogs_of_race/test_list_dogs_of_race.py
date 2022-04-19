import allure
import pytest
from application_settings.api_application_settings import CustomTestApplicationSettingsProvider
from test_data.api_test_data.game_api_data import GameData
from utils.logger import CustomLogger

logger = CustomLogger('api_test').get_logger()


class TestListDogsOfRace(GameData):

    next_match_api = CustomTestApplicationSettingsProvider('/game/api/match')

    @allure.step('Successful retrieve list of dogs races')
    def test_list_of_dogs_race(self):
        random_match_id = self.next_match_api.get_request()['response']['matchId']
        api = CustomTestApplicationSettingsProvider('/game/api/dog/{}'.format("6246a6dbc6ba425e4148ee82"))
        result = api.get_request()
        try:
            assert result['status_code'] == 200
            assert len(result['response']) > 1
            logger.info("Dogs of a match retrieved successfully")
        except Exception as e:
            logger.error(f"Failed retrieving dog list {e}")
            raise AssertionError
