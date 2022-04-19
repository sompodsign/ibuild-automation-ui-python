import time

import allure
from application_settings.api_application_settings import CustomTestApplicationSettingsProvider
from data_provider.test_data_provider import CustomTestDataProvider
from utils.logger import CustomLogger
import pytest

logger = CustomLogger('api_test').get_logger()


class TestVerifyEmail(CustomTestDataProvider):
    verify_otp_api = CustomTestApplicationSettingsProvider('/auth/api/verify/otp')
    verify_email_api = CustomTestApplicationSettingsProvider('/auth/api/verify/email')

    @allure.step("This test verifies that OTP validation works properly")
    @pytest.mark.skip
    def test_successful_otp_verification(self):
        email_result = self.verify_email_api.post_request(payload=self.get_email_for_otp_send())
        email_response = email_result["status_code"]
        assert email_response == 201
        logger.info("Please wait a while for the email to be sent")
        time.sleep(40)
        otp = self.get_otp()
        headers = self.get_headers()
        headers["Authorization"] = "Bearer " + email_result["response"]["data"]
        otp_response = self.verify_otp_api.post_request(payload={"otp": otp}, headers=headers)
        response = otp_response['status_code']
        try:
            assert response == 201
            assert otp_response['response']['message'] == 'Otp verified successfully '
            assert otp_response['response']['success'] is True
            logger.info("OTP verification successful")
        except AssertionError:
            logger.error("OTP verification failed")
            raise AssertionError

    @allure.step("THis test verifies that OTP can't be validated with invalid code")
    def test_otp_verification_with_invalid_otp(self):
        otp_response = self.verify_otp_api.post_request(self.get_invalid_otp(), self.get_headers_with_user_token())
        response = otp_response['status_code']
        try:
            assert response == 401
            logger.info("OTP verification not successful")
        except AssertionError:
            logger.error("OTP verification Successful with invalid otp")
            raise AssertionError


    # @allure.step('Failed verify otp with no token')
    # def test_026_verify_otp():
    #     otp_api = VerifyOtpApi("/auth/api/verify/otp")
    #     result = otp_api.post_request(payload=invalid_otp)
    #     status_code = result['status_code']
    #     assert status_code == 400
    #
    #
    # @allure.step('Failed verify otp with get request')
    # def test_027_verify_otp():
    #     otp_api = VerifyOtpApi("/auth/api/verify/otp")
    #     result = otp_api.get_request(headers=headers_with_token, payload=invalid_otp)
    #     status_code = result['status_code']
    #     assert status_code == 400
    #
    #
    # @allure.step('Failed verify otp with put request')
    # def test_028_verify_otp():
    #     otp_api = VerifyOtpApi("/auth/api/verify/otp")
    #     result = otp_api.put_request(headers=headers_with_token, payload=invalid_otp)
    #     status_code = result['status_code']
    #     assert status_code == 400
    #
    #
    # @allure.step('Failed verify otp with put request')
    # def test_029_verify_otp():
    #     otp_api = VerifyOtpApi("/auth/api/verify/otp")
    #     result = otp_api.delete_request()
    #     status_code = result['status_code']
    #     assert status_code == 404
