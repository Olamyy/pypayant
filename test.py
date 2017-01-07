import unittest
from unittest import TestCase

from pypayant import config
from pypayant.base import BasePayantAPI
from pypayant.errors import AuthKeyError
from pypayant.client import Client
from pypayant.invoice import Invoice
try:
    from mock import patch, MagicMock
except ImportError:
    from unittest.mock import patch, MagicMock

base_url = {
    "demo": "https://api.demo.payant.ng/",
    "live": "https://api.payant.ng/"
}


class MockRequest:
    def __init__(self, response, status_code=200, **kwargs):
        self.response = response
        self.overwrite = False
        if kwargs.get('overwrite'):
            self.overwrite = True
        self.status_code = status_code

    @classmethod
    def raise_for_status(cls):
        pass

    def json(self):
        if self.overwrite:
            return self.response
        return {'data': self.response}


class TestBaseAPI(TestCase):
    def test_raise_auth_key(self):
        with self.assertRaises(AuthKeyError):
            BasePayantAPI()

    def test_path(self):
        self.base_url = base_url
        self.base_api = BasePayantAPI(
            auth_key=config.demo_auth_key, implementation="demo")
        path = self.base_api._path("payment")
        self.assertEquals(
            path, self.base_url[self.base_api.implementation] + "payment")


class BaseCallTestCase(TestCase):
    def setUp(self):
        self.patcher = patch('pypayant.base.requests.post')
        self.mock_post = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def mock_response(self, data, **kwargs):
        return MockRequest(data, **kwargs)


class TestClientReal(TestCase):
    def test_add_new_client_successfully1(self):
        base = Client(auth_key=config.demo_auth_key)
        datas = base.add(email=config.test_user["email"],
                         first_name=config.test_user["first_name"],
                         last_name=config.test_user["last_name"],
                         phone=config.test_user["phone"])


class TestClient(BaseCallTestCase):
    def test_add_new_client_successfully(self):
        self.mock_post.return_value = self.mock_response(
            {
                'message': "Client created successfully.",
                "status": "success",
                "data": config.test_user
            },
            overwrite=True)

        base = Client(auth_key=config.demo_auth_key)
        code, status, message, client = base.add(
            email=config.test_user["email"],
            first_name=config.test_user["first_name"],
            last_name=config.test_user["last_name"],
            phone=config.test_user["phone"])
        self.assertEquals(client, config.test_user)
        self.assertEqual(code, 200),
        self.assertEqual(status, 'success')
        self.assertEqual(message, "Client created successfully.")

    def test_when_existing_user_exists(self):
        self.mock_post.return_value = self.mock_response(
            {
                'message': "Client already exist.",
                'status': 'error'
            },
            overwrite=True)
        base = Client(auth_key=config.demo_auth_key)
        code, status, message = base.add(
            email=config.test_user["email"],
            first_name=config.test_user["first_name"],
            last_name=config.test_user["last_name"],
            phone=config.test_user["phone"])
        self.assertEqual(code, 200)
        self.assertEqual(status, 'error')
        self.assertEqual(message, "Client already exist.")

    def test_get(self):
        base = Client(auth_key=config.demo_auth_key)
        # client = base.edit(1)


    # class TestInvoice(BaseCallTestCase):
class TestInvoice(TestCase):
    def setUp(self):
        super(TestInvoice, self).setUp()
        self.base = Invoice(auth_key=config.demo_auth_key)

    def test_create(self):
        client = self.base.add(client_id=1,
                               due_date="12/30/2016",
                               fee_bearer="client",
                               items={
                                   "name": "Website Design",
                                   "description":
                                   "5 Pages Website plus 1 Year Web Hosting",
                                   "unit_cost": "50000.00",
                                   "quantity": "1"
                               })

    def test_invoice_creation_with_error_message(self):
        self.mock_post.return_value = self.mock_response(
            {
                'message': "Client created successfully.",
                "status": "success",
                "data": config.test_user
            },
            overwrite=True)


if __name__ == '__main__':
    unittest.main()