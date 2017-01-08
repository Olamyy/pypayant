from __future__ import print_function  # (at top of module)
import os
import requests
import json
from pypayant import __version__
from pypayant.errors import AuthKeyError, HttpMethodError


class BasePayantAPI(object):
    """

    """

    _content_type = "application/json"
    _base_url = {
        "demo": "https://api.demo.payant.ng/",
        "live": "https://api.payant.ng/"
    }

    def __init__(self, auth_key=None, implementation="demo"):
        if not auth_key:
            raise AuthKeyError("Authentication key is not provided.")
        else:
            self.auth_key = os.getenv("PAYANT_AUTH_KEY", None)
        if auth_key:
            self.auth_key = auth_key
        self.implementation = implementation

    def _path(self, path):
        url_path = self._base_url.get(self.implementation)
        return url_path + path

    def http_headers(self):
        return {
            "Content-Type": self._content_type,
            "Authorization": "Bearer " + self.auth_key,
            "user-agent": "pyPayant-{}".format(__version__)
        }

    def _json_parser(self, json_response):
        """Only the status code, the status of the requst and the data
        is sent back. the message is irrelevant if ths request was successful"""
        response = json_response.json()
        status = response.get('status', None)
        message = response.get('message', None)
        data = response.get('data', None)

        return json_response.status_code, status, data

    def _exec_request(self, method, url, data=None):
        method_map = {
            'GET': requests.get,
            'POST': requests.post,
            'PUT': requests.put,
            'DELETE': requests.delete
        }

        payload = json.dumps(data) if data else data
        request = method_map.get(method)

        if not request:
            raise HttpMethodError(
                "Request method not recognised or implemented")

        response = request(
            url, headers=self.http_headers(), data=payload, verify=True)
        if response.status_code == 404:
            msg = "The object request cannot be found"
            if response.json().get('message'):
                body = response.json()
            return response.status_code, body['status'], body['message']
            # return response.status_code, False, msg, None
        body = response.json()
        # import pdb; pdb.set_trace()
        if body.get('status') == 'error':
            return response.status_code, body['status'], body['message']
        if response.status_code in [200, 201]:
            return self._json_parser(response)
        response.raise_for_status()