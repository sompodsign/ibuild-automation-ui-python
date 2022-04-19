import allure
from application_settings.api_application_settings import CustomTestApplicationSettingsProvider
from test_data.api_test_data.game_api_data import GameData

from utils.logger import CustomLogger
logger = CustomLogger('api_test').get_logger()


class TestSaveDog(GameData):
    # race_api = ApiTestApplicationSettingsProvider('/game/api/race')
    dog_api = CustomTestApplicationSettingsProvider('/game/api/dog')

    @allure.step('Successful dog saving with right details')
    def test_dog_save(self):
        # races = self.race_api.get_request()
        # match_id = races['response']['races'][-1]['_id']
        result = self.dog_api.post_request(self.get_new_dog_data())
        status_code = result['status_code']
        try:
            assert status_code == 201
            assert 'Dog Saved successfully' in result['response']['message']
            assert result['response']['success'] is True
            logger.info('Dog Saved successfully')
        except AssertionError as e:
            logger.error(f"Dog is not successfully saved: {e}")
            assert AssertionError

    @allure.step('Failed dog saving without name test')
    def test_dog_save_without_name(self):
        result = self.dog_api.post_request(self.get_new_dog_data_without_name())
        try:
            assert result['status_code'] == 400
            assert result['response']['message'] == ['name should not be empty']
            logger.info('Dog name is required')
        except AssertionError as e:
            logger.error(f"Dog is saved without a name: {e}")
            assert AssertionError

    @allure.step('Failed dog saving without weight')
    def test_dog_save_without_weight(self):
        result = self.dog_api.post_request(self.get_new_dog_data_without_weight())
        try:
            assert result['status_code'] == 400
            assert result['response']['message'] == ['weight should not be empty']
            logger.info('Dog weight is required, not saved')
        except AssertionError as e:
            logger.error(f"Dog is saved without a weight: {e}")
            assert AssertionError

    @allure.step('Failed dog saving without fatigue')
    def test_dog_save_without_fatigue(self):
        result = self.dog_api.post_request(self.get_new_dog_data_without_fatigue())
        try:
            assert result['status_code'] == 400
            assert result['response']['message'] == ['fatigue should not be empty']
            logger.info('Dog fatigue is required, not saved')
        except AssertionError as e:
            logger.error(f"Dog is saved without a fatigue: {e}")
            assert AssertionError

    @allure.step('Failed dog saving without injury')
    def test_dog_save_without_injury(self):
        result = self.dog_api.post_request(self.get_new_dog_data_without_injury())
        try:
            assert result['status_code'] == 400
            assert result['response']['message'] == ['injury should not be empty']
            logger.info('Dog injury is required, not saved')
        except AssertionError as e:
            logger.error(f"Dog is saved without a injury: {e}")
            assert AssertionError

    @allure.step('Failed dog saving without acceleration')
    def test_dog_save_without_acceleration(self):
        result = self.dog_api.post_request(self.get_new_dog_data_without_acceleration())
        try:
            assert result['status_code'] == 400
            assert result['response']['message'] == ['acceleration should not be empty']
            logger.info('Dog acceleration is required, not saved')
        except AssertionError as e:
            logger.error(f"Dog is saved without a acceleration: {e}")
            assert AssertionError

    @allure.step('Failed dog saving without topSpeed')
    def test_dog_save_without_topSpeed(self):
        result = self.dog_api.post_request(self.get_new_dog_data_without_top_speed())
        try:
            assert result['status_code'] == 400
            assert result['response']['message'] == ['topSpeed should not be empty']
            logger.info('Dog topSpeed is required, not saved')
        except AssertionError as e:
            logger.error(f"Dog is saved without a topSpeed: {e}")
            assert AssertionError

    @allure.step('Failed dog saving without age')
    def test_dog_save_without_age(self):
        result = self.dog_api.post_request(self.get_new_dog_data_without_age())
        try:
            assert result['status_code'] == 400
            assert result['response']['message'] == ['age should not be empty']
            logger.info('Dog age is required, not saved')
        except AssertionError as e:
            logger.error(f"Dog is saved without a age: {e}")
            assert AssertionError

    @allure.step('Failed dog saving without power')
    def test_dog_save_without_power(self):
        result = self.dog_api.post_request(self.get_new_dog_data_without_power())
        try:
            assert result['status_code'] == 400
            assert result['response']['message'] == ['power should not be empty']
            logger.info('Dog power is required, not saved')
        except AssertionError as e:
            logger.error(f"Dog is saved without a power: {e}")
            assert AssertionError

    @allure.step('Failed dog saving without mainWeather')
    def test_dog_save_without_main_weather(self):
        result = self.dog_api.post_request(self.get_new_dog_data_without_main_weather())
        try:
            assert result['status_code'] == 400
            assert result['response']['message'] == ['mainWeather should not be empty']
            logger.info('Dog mainWeather is required, not saved')
        except AssertionError as e:
            logger.error(f"Dog is saved without a mainWeather: {e}")
            assert AssertionError

    @allure.step('Failed dog saving without sex')
    def test_dog_save_without_sex(self):
        result = self.dog_api.post_request(self.get_new_dog_data_without_sex())
        try:
            assert result['status_code'] == 400
            assert result['response']['message'] == ['sex should not be empty']
            logger.info('Without sex data dog can not save')
        except AssertionError as e:
            logger.error(f"Dog is saved without sex data: {e}")
            raise AssertionError

    @allure.step('Failed dog saving without matchId')
    def test_dog_save_without_match_id(self):
        result = self.dog_api.post_request(self.get_new_dog_data_without_matchId())
        try:
            assert result['status_code'] == 400
            assert result['response'] == ['matchId should not be empty']
            logger.info('Without matchId data dog can not save')
        except AssertionError as e:
            logger.error(f"Dog is saved without matchId: {e}")
            raise AssertionError

    @allure.step("Delete dog success test")
    def test_dog_delete(self):
        result = self.dog_api.post_request(self.get_new_dog_data())
        dog_id = result['response']['id']
        dog_delete_api = CustomTestApplicationSettingsProvider('/game/api/dog/{}'.format(dog_id))
        delete_result = dog_delete_api.delete_request()
        try:
            assert delete_result['status_code'] == 200
            assert delete_result['response']['message'] == 'Dog deleted successfully'
            logger.info("Dog deleted successfully")
        except Exception as e:
            logger.error("Dog not deleted", e)
