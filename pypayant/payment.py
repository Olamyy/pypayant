import requests

from pypayant import config
from pypayant.base import BasePayantAPI


class Payment(BasePayantAPI):
    def __init__(self, auth_key):
        super(Payment, self).__init__(auth_key)
        self.base_payment_key = "payments"

    def add(self, reference_code, date, amount, channel):
        """

        :param reference_code:
        :param date:
        :param amount:
        :param channel:
        :return:
        """
        url = self._path(self.base_payment_key)
        print url
        request_data = {
                        "reference_code": reference_code,
                        "date": date,
                        "amount": amount,
                        "channel": channel
                       }
        return self._exec_request('POST', url, request_data)
        # return requests.request('POST', url, data=request_data)

test = Payment(auth_key=config.demo_auth_key)
print test.add(reference_code="j9CbiTN0oJe4vWhglyS2", date="12/21/2016",
            amount="50,0000", channel="Cash")
