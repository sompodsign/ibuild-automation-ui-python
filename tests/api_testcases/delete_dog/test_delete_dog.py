# import allure
# from application_settings.api_application_settings import ApiTestApplicationSettingsProvider
#
# from utils.logger import CustomLogger
# logger = CustomLogger('api_test').get_logger()
#
#
# class TestDeleteDog:
#
#     api = ApiTestApplicationSettingsProvider('/game/api/match')
#
#     @allure.step('Successful next match retrieve')
#     def test_next_match(self):
#         result = self.api.get_request()
#         status_code = result['status_code']
#         try:
#             assert status_code == 200
#             assert isinstance(result['response']['matchId'], str)
#             logger.info('Next match retrieved successfully')
#         except AssertionError as e:
#             logger.error(f"Next match not retrieved something is wrong: {e}")
#             assert AssertionError
