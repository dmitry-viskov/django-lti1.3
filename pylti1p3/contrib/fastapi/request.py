from pylti1p3.request import Request


class FastAPIRequest(Request):
    _session = None

    def __init__(self, request):
        super().__init__()
        self._request = request

    @property
    def session(self):
        return self._request.session

    async def get_param(self, key):
        if self._request.method == "GET":
            return self._request.query_params.get(key, None)
        return (await self._request.form()).get(key)

    def get_cookie(self, key):
        return self._request.cookies.get(key, None)

    def is_secure(self):
        return self._request.url.is_secure
