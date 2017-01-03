from unittest import TestCase
from pypayant.base import BasePyantAPI
from pypayant.errors import AuthKeyError
base_url = {
    "demo": "https://api.demo.payant.ng",
    "live": "https://api.payant.ng"
}


class TestBaseAPI(TestCase):
    def setUp(self):
        super(TestBaseAPI, self).setUp()
        self.base_url = base_url
        self.base_api = BasePyantAPI(auth_key=None, implementation="demo")

    def test_raise_auth_key(self):
        self.assertRaises(AuthKeyError, BasePyantAPI())

    def test_path(self):
        path = self.base_api._path("payment")
        self.assertEquals(path, self.base_url[self.base_api.implementation])


tester = TestBaseAPI()
# tester.setUp()