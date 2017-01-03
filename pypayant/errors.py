class PyPayantError(Exception):
    def __init__(self, message=None, http_status=None):
        super(PyPayantError, self).__init__(message)

        self.message = message
        self.http_status = http_status


class AuthKeyError(PyPayantError):
    """
    Auth Key Not Provided
    """
    pass


class HttpMethodError(PyPayantError):
    pass

