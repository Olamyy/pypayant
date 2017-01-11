from __future__ import print_function  # (at top of module)
from .base import BasePayantAPI

class Client(BasePayantAPI):

    def __init__(self, auth_key):
        super(Client, self).__init__(auth_key)
        self.base_client_key = "clients"

    def add(self, first_name, last_name, email, phone,
            website=None, address=None, Type=None, settlement_bank=None,
            account_number=None, company_name=None):
        """

        Creates a new payant client
        :param website:
        :param first_name:
        :param last_name:
        :param email:
        :param phone:
        :param address:
        :param Type:
        :param settlement_bank:
        :param account_number:
        :param company_Name:
        :return:
        """
        url = self._path(self.base_client_key)
        print(url)
        request_data = {
            "company_name": company_name,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "website": website,
            "address": address,
            "type": Type,
            "settlement_bank": settlement_bank,
            "account_number": account_number
        }
        return self._exec_request('POST', url, request_data)

    def get(self, client_id):
        """
        Get details of a client with the id provided
        :param client_id:
        :return:
        """
        url = self._path("{0}/{1}".format(self.base_client_key, client_id))
        return self._exec_request('GET', url)

    def edit(self,
             client_id,
             first_name,
             last_name,
             email,
             phone,
             website=None,
             address=None,
             Type=None, 
             settlement_bank=None,
             account_number=None, 
             company_name=None):
        """
        Update a Payant client with the client_id provided
        :param client_id:
        :param first_name:
        :param last_name:
        :param email:
        :param phone:
        :param website:
        :param address:
        :param Type:
        :param settlement_bank:
        :param account_number:
        :param company_Name:
        :return:
        """
        url = self._path("{0}/{1}".format(self.base_client_key, client_id))
        request_data = {
            "company_name": company_Name,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "website": website,
            "address": address,
            "type": Type,
            "settlement_bank": settlement_bank,
            "account_number": account_number
        }
        return self._exec_request('PUT', url, request_data)

    def delete(self, client_id):
        url = self._path("{0}/{1}".format(self.base_client_key, client_id))
        return self._exec_request('DELETE', url)
