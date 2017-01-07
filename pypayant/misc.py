from pypayant.base import BasePayantAPI


class Misc(BasePayantAPI):
    def __init__(self, auth_key):
        super(Misc, self).__init__(auth_key)

    def get_states(self):
        """

        :return: state_id
        """
        url = self._path("states")
        return self._exec_request('GET', url)

    def get_lga(self, state_id):
        """
        :param: state_id
        :return:
        """
        url = self._path("lga")
        request_data = {
            "state_id": state_id,
        }
        return self._exec_request('POST', url, request_data)
