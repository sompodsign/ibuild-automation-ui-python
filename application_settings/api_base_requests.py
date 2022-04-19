import requests
import json
from application_settings.application_settings import ApplicationSettings


class BaseApi(object):
    """
    this Base api class is serving basic attributes for every single api page inherited from this class

    """
    application_settings = ApplicationSettings()
    base_url = application_settings.get_api_base_url()
    HEADERS = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def __init__(self, url):
        self.url = self.base_url + url

    def get_request(self, payload=None, headers=None):
        if headers is None:
            headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        if payload is None:
            response = requests.request("GET", self.url, headers=headers)
        else:
            response = requests.request("GET", self.url, data=json.dumps(payload), headers=headers)
        return self.get_response(response)

    def post_request(self, payload=None, headers=None):
        if headers is None:
            headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        if payload is None:
            response = requests.request("POST", self.url, headers=headers)
        else:
            response = requests.request("POST", self.url, data=json.dumps(payload), headers=headers)
        return self.get_response(response)

    def put_request(self, payload=None, headers=None):
        if headers is None:
            headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        if payload is None:
            response = requests.request("PUT", self.url, headers=headers)
        else:
            response = requests.request("PUT", self.url, data=json.dumps(payload), headers=headers)
        return self.get_response(response)

    def delete_request(self, headers=None):
        if headers is None:
            headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        response = requests.request('DELETE', self.url, headers=headers)
        return self.get_response(response)

    def patch_request(self, payload=None, headers=None):
        if headers is None:
            headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        if payload is None:
            response = requests.request("PATCH", self.url, headers=headers)
        else:
            response = requests.request("PATCH", self.url, data=json.dumps(payload), headers=headers)
        return self.get_response(response)

    @staticmethod
    def get_response(response):
        return {"status_code": response.status_code, "response": response.json()}

    def __str__(self):
        return self.url
