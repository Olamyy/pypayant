from pypayant.base import BasePayantAPI


class Misc(BasePayantAPI):
    def __init__(self, auth_key):
        super(Misc, self).__init__(auth_key)

    def get_banks(self):
        """

        :return: state_id
        """
        url = self._path("banks")
        return self._exec_request('GET', url)
