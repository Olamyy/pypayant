import unittest
from unittest import TestCase

from pypayant import config
from pypayant.base import BasePayantAPI
from pypayant.errors import AuthKeyError
from pypayant.client import Client
from pypayant.invoice import Invoice

base_url = {
    "demo": "https://api.demo.payant.ng/",
    "live": "https://api.payant.ng/"
}


class TestBaseAPI(TestCase):
    def test_raise_auth_key(self):
        self.assertRaises(BasePayantAPI(), AuthKeyError)

    def test_path(self):
        self.base_url = base_url
        self.base_api = BasePayantAPI(
            auth_key=config.demo_auth_key, implementation="demo")
        path = self.base_api._path("payment")
        self.assertEquals(
            path, self.base_url[self.base_api.implementation] + "payment")


class TestClient(TestCase):
    def test_add(self):

        base = Client(auth_key=config.demo_auth_key)
        client = base.add(email=config.test_user["email"],
                          first_name=config.test_user["first_name"],
                          last_name=config.test_user["last_name"],
                          phone=config.test_user["phone"])
        self.assertEquals(client, config.test_user)

    def test_get(self):
        base = Client(auth_key=config.demo_auth_key)
        # client = base.edit(1)


class TestInvoice(TestCase):
    def test_create(self):
        base = Invoice(auth_key=config.demo_auth_key)
        client = base.add(client_id=1,
                          due_date="12/30/2016",
                          fee_bearer="client",
                          items={
                              "name": "Website Design",
                              "description":
                              "5 Pages Website plus 1 Year Web Hosting",
                              "unit_cost": "50000.00",
                              "quantity": "1"
                          })


if __name__ == '__main__':
    unittest.main()