import allure
from application_settings.api_application_settings import CustomTestApplicationSettingsProvider
from data_provider.test_data_provider import CustomTestDataProvider
from utils.logger import CustomLogger

logger = CustomLogger('api_test').get_logger()


class TestUserLogin(CustomTestDataProvider):

    user_api = CustomTestApplicationSettingsProvider('/auth/api/login')

    @allure.step('Successful user login_test with valid data test')
    def test_valid_signin(self):
        result = self.user_api.post_request(payload=self.get_user_sign_in_data())
        status_code = result['status_code']
        try:
            assert status_code == 201
            assert result['response']['message'] == "User logged in successfully"
            logger.info("Successful user login test with valid data")
        except AssertionError as e:
            logger.error(f"Failed user login_test with valid data test: {e}")
            assert False

    @allure.step('Fail sign in without username')
    def test_sign_in_without_email(self):
        result = self.user_api.post_request(self.get_sign_in_data_without_email())
        status_code = result['status_code']
        try:
            assert status_code == 400
            assert result['response']['message'][0] == "email should not be empty"
            logger.info("Failed sign in without email")
        except AssertionError as e:
            logger.error(f"Failed sign in without email test: {e}")
            assert False

    @allure.step('Fail sign in without password')
    def test_sign_in_without_password(self):
        result = self.user_api.post_request(payload=self.get_sign_in_data_without_password())
        status_code = result['status_code']
        try:
            assert status_code == 400
            assert result['response']['message'][0] == "password should not be empty"
            logger.info("Failed sign in without password")
        except AssertionError as e:
            logger.error(f"Failed sign in without password test: {e}")
            assert False

    @allure.step('Fail sign in get request')
    def test_invalid_sign_in_get_request(self):
        result = self.user_api.get_request(payload=self.get_sign_in_data_without_password())
        status_code = result['status_code']
        try:
            assert status_code == 404
            logger.info("Failed sign in with get request")
        except AssertionError as e:
            logger.error(f"Signed in with get request test: {e}")
            assert False

    @allure.step('Fail sign in put request')
    def test_invalid_sign_in_put_request(self):
        result = self.user_api.put_request(payload=self.get_sign_in_data_without_password())
        status_code = result['status_code']
        try:
            assert status_code == 404
            logger.info("Failed sign in with put request")
        except AssertionError as e:
            logger.error(f"Signed in with put request test: {e}")
            assert False

    @allure.step('Fail sign in delete')
    def test_invalid_sign_in_delete_request(self):
        result = self.user_api.delete_request()
        status_code = result['status_code']
        try:
            assert status_code == 404
            logger.info("Failed sign in with delete request")
        except AssertionError as e:
            logger.error(f"Signed in with delete request test: {e}")
