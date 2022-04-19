import allure
from application_settings.api_application_settings import CustomTestApplicationSettingsProvider
from data_provider.test_data_provider import CustomTestDataProvider
from utils.logger import CustomLogger

logger = CustomLogger('api_test').get_logger()


class TestVerifyEmail(CustomTestDataProvider):
    verify_api = CustomTestApplicationSettingsProvider('/auth/api/verify/email')

    @allure.step('This test verifies that email verification sends OTP to email')
    def test_successful_player_sign_up(self):
        result = self.verify_api.post_request(self.get_email_for_otp_send())
        response = result["status_code"]
        try:
            assert response == 201
            assert result["response"]["message"] == 'Otp successfully sent to your mail '
            logger.info('Otp successfully sent to your registered email address')
        except AssertionError:
            logger.error('Otp not sent to your mail ')
            raise AssertionError

    @allure.step('This test verifies that OTP does not send to non registered email')
    def test_unsuccessful_otp_send_to_non_registered_email(self):
        result = self.verify_api.post_request(self.get_non_registered_email_object_for_otp_send())
        response = result["status_code"]
        try:
            assert response == 400
            assert result["response"]["message"] == 'Could not find your Account'
            logger.info('Email not registered so OTP not sent')
        except AssertionError:
            logger.error('OTP sent to non registered email')
            raise AssertionError

    @allure.step('This test verifies that OTP does not send to an invalid email')
    def test_unsuccessful_otp_send_to_invalid_email(self):
        result = self.verify_api.post_request(self.get_invalid_email_object_for_otp_send())
        response = result["status_code"]
        try:
            assert response == 400
            assert result["response"]["message"] == 'Could not find your Account'
            logger.info('OTP not sent to invalid email')
        except AssertionError:
            logger.error('OTP sent to invalid email')
            raise AssertionError
