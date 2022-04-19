# import random
#
# import allure
# from application_settings.api_application_settings import ApiTestApplicationSettingsProvider
# from test_data.api_test_data.game_api_data import GameData
#
# from utils.logger import CustomLogger
# logger = CustomLogger('api_test').get_logger()
#
#
# class TestNextMatch(GameData):
#
#     next_match_api = ApiTestApplicationSettingsProvider('/game/api/match')
#
#     @allure.step('Successful next match retrieve')
#     def test_bet_on_a_dog_of_a_match(self):
#
#         result = self.next_match_api.get_request()
#         match_id = result['response']['matchId']
#         dog_id = random.choice(result['response']['dogs'])['id']
#         api = ApiTestApplicationSettingsProvider('/game/api/bet/{}/{}'.format(dog_id, match_id))
#         result = api.put_request(self.get_bet_amount(), self.get_headers_with_user_token())
#         status_code = result['status_code']
#         try:
#             assert status_code == 200
#             assert isinstance(result['response']['matchId'], str)
#             logger.info('Next match retrieved successfully')
#         except AssertionError as e:
#             logger.error(f"Next match not retrieved something is wrong: {e}")
#             assert AssertionError
