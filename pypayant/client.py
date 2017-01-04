from requests import request

from base import BasePyantAPI


class Client(BasePyantAPI):
    def __init__(self):
        super(Client, self).__init__()
        self.base_url_key = "/clients"

    def create(self, first_name, last_name, email, phone, website=None, address=None, state=None, lga=None,
               company_Name=None):
        """
        Creates a new payant client

        :param first_name:
        :param last_name:
        :param email:
        :param phone:
        :param address:
        :param state:
        :param lga:
        :param company_Name:
        :return:
        """
        url = self._path(self.base_url_key)
        request_data = {"company_name": company_Name,
                        "first_name": first_name,
                        "last_name": last_name,
                        "email": email,
                        "phone": phone,
                        "website": website,
                        "address": address,
                        "state": state,
                        "lga": lga
                        }
        # response = request(url="https://api.demo.payant.ng/clients", method="POST", data=request_data, verify=True)
        # return response

        return self._exec_request('POST', url, request_data)

    def get(self, client_id):
        """
        Get details of a client with the id provided
        :param client_id:
        :return:
        """
        url = self._path("{0}/{1}".format(self.base_url_key,client_id))
        return self._exec_request('GET', url)

    def update(self,client_id, first_name, last_name, email, phone, website=None, address=None, state=None, lga=None,
               company_Name=None):
        """
        Update a Payant client with the client_id provided
        :param client_id:
        :param first_name:
        :param last_name:
        :param email:
        :param phone:
        :param website:
        :param address:
        :param state:
        :param lga:
        :param company_Name:
        :return:
        """
        url = self._path("{0}/{1}".format(self.base_url_key,client_id))
        request_data = {
            "company_name": company_Name,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "website": website,
            "address": address,
            "state": state,
            "lga": lga
        }
        return self._exec_request('PUT', url, request_data)

    def delete(self, client_id):
        url = self._path("{0}/{1}".format(self.base_url_key, client_id))
        return self._exec_request('DELETE', url)


