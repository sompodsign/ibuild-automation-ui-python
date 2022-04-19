from .api_base_requests import BaseApi
from data_provider.test_data_provider import CustomTestDataProvider


class CustomTestApplicationSettingsProvider(BaseApi, CustomTestDataProvider):
    """
    Class to handle or share all necessary API application settings
    """

    def __init__(self, endpoint):
        super().__init__(endpoint)

    def get_user_token(self):
        response = self.post_request(payload=self.get_user_sign_in_data())
        return response['response']['data']

    def get_admin_token(self):
        response = self.post_request(payload={})
        return response.json()['accessToken']

    def get_headers_with_user_token(self):
        headers_with_user_token = {'Authorization': self.get_user_token(), 'Content-Type': 'application/json',
                                   'Accept': 'application/json'}
        return headers_with_user_token

    def get_headers_with_admin_token(self):
        headers_with_admin_token = {'Authorization': self.get_admin_token(), 'Content-Type': 'application/json',
                                    'Accept': 'application/json'}
        return headers_with_admin_token

    @staticmethod
    def get_headers():
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        return headers

    def current_user_id(self):
        response = self.post_request(payload={})
        return response.json()['userId']
