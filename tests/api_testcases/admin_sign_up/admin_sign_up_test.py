
import allure

from application_settings.api_application_settings import CustomTestApplicationSettingsProvider
from data_provider.test_data_provider import CustomTestDataProvider
from utils.logger import CustomLogger

logger = CustomLogger('api_test').get_logger()


class TestAdminSignUp(CustomTestDataProvider):
    admin_api = CustomTestApplicationSettingsProvider('/auth/api/admin/signup')

    @allure.step('This test verifies that users can sign up as a admin.')
    def test_successful_gambler_sign_up(self):
        result = self.admin_api.post_request(self.get_new_valid_register_data())
        response = result["status_code"]
        try:
            assert response == 201
            assert result["response"]["message"] == "user created successfully"
            logger.info("admin sign up was successful.")
        except AssertionError as e:
            logger.error(result["response"]["message"], e)
            assert False

    @allure.step("This test verifies that user can't sign up as aadmin with an existing email.")
    def test_existing_admin_sign_up(self):
        result = self.admin_api.post_request(self.get_new_register_data_with_existing_email())
        response = result["status_code"]
        try:
            assert response == 409
            assert result["response"]["message"] == "User already exists"
            assert result["response"]["error"] == "Conflict"
            logger.info("existing admin sign up was unsuccessful.")
        except AssertionError as e:
            logger.error(result["response"]["message"], e)
            assert False

    @allure.step("This test verifies that user can't sign up as a admin without username")
    def test_admin_sign_up_without_username(self):
        result = self.admin_api.post_request(self.get_new_register_data_without_username())
        response = result["status_code"]
        try:
            assert response == 400
            assert result["response"]["message"][0] == "username should not be empty"
            logger.info("admin can't sign up without username.")
        except AssertionError as e:
            logger.error(result["response"]["message"], e)
            assert False

    @allure.step("This test verifies that user can't sign up as aadmin without email")
    def test_admin_sign_up_without_email(self):
        result = self.admin_api.post_request(self.get_new_register_data_without_email())
        response = result["status_code"]
        try:
            assert response == 400
            assert result["response"]["message"][0] == "email must be an email"
            logger.info("admin can't sign up without email.")
        except AssertionError as e:
            logger.error(result["response"]["message"], e)
            assert False

    @allure.step("This test verifies that user can't sign up as admin without password")
    def test_gambler_sign_up_without_password(self):
        result = self.admin_api.post_request(self.get_new_register_data_without_password())
        response = result["status_code"]
        try:
            assert response == 400
            assert result["response"]["message"] == ['password should not be empty', 'password must be longer than or equal to 6 characters']
            logger.info("admin can't sign up without password.")
        except AssertionError as e:
            logger.error(result["response"]["message"], e)
            assert False

    @allure.step("This test verifies that user can't sign up with put request")
    def test_admin_sign_up_put_request(self):
        result = self.admin_api.put_request(self.get_new_valid_register_data())
        response = result["status_code"]
        try:
            assert response == 404
            assert result["response"]["message"] == 'Cannot PUT /auth/api/admin/signup'
            logger.info("admin can't sign up with put request.")
        except AssertionError as e:
            logger.error(result["response"]["message"], e)
            assert False

    @allure.step("This test verifies that user can't sign up with delete request")
    def test_admin_sign_up_delete_request(self):
        result = self.admin_api.delete_request(self.get_new_valid_register_data())
        response = result["status_code"]
        try:
            assert response == 404
            assert result["response"]["message"] == 'Cannot DELETE /auth/api/admin/signup'
            logger.info("gambler can't sign up with delete request.")
        except AssertionError as e:
            logger.error(result["response"]["message"], e)
            assert False
