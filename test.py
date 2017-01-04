import unittest
from unittest import TestCase

from pypayant import config
from pypayant.base import BasePyantAPI
from pypayant.errors import AuthKeyError
from pypayant.client import Client

base_url = {
    "demo": "https://api.demo.payant.ng/",
    "live": "https://api.payant.ng/"
}


class TestBaseAPI(TestCase):
    # def __init__(self):
    #     super(TestBaseAPI).__init__()
    #     self.base_url = base_url
    #     self.base_api = BasePyantAPI(auth_key=None, implementation="demo")

    def test_raise_auth_key(self):
        self.assertRaises(AuthKeyError, BasePyantAPI())

    def test_path(self):
        self.base_url = base_url
        self.base_api = BasePyantAPI(auth_key=config.demo_auth_key, implementation="demo")
        path = self.base_api._path("payment")
        self.assertEquals(path, self.base_url[self.base_api.implementation]+ "payment")


class TestClient(TestCase):
    def test_create(self):
       
        base = Client(auth_key=config.demo_auth_key)
        client = base.create(email=config.test_user["email"], first_name=config.test_user["first_name"],last_name=config.test_user["last_name"],
                             phone=config.test_user["phone"])
        # self.assertEquals(client, )

    def test_get(self):
        base = Client(auth_key=config.demo_auth_key)
        client = base.get(1)
#         self.assertEquals({
#   "status": "success",
#   "data": {
#     "id": 1,
#     "company_id": 1,
#     "name": "Albert Specialist Hospital",
#     "first_name": "Albert",
#     "last_name": "Jane",
#     "email": "jane@alberthospital.com",
#     "phone": "+2348012345678",
#     "website": "http://www.alberthospital.com",
#     "address": "Wase II",
#     "state": "37",
#     "lga": "782",
#     "status": "1",
#     "created_at": "2016-12-21 17:19:10",
#     "updated_at": "2016-12-21 17:19:10",
#     "deleted_at": None
#   }
# }
#    ,client)


if __name__ == '__main__':
    unittest.main()