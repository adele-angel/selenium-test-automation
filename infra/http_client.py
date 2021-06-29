import requests
from requests import Response


class HttpCommand:
    def __init__(self):
        self.headers: dict = {}
        self.auth = None
        self.body = None
        self.route = ''
        self.method = 'GET'

    def set_headers(self, headers: dict):
        self.headers = headers
        return self

    def set_auth(self, auth):
        self.auth = auth
        return self

    def set_body(self, body):
        self.body = body
        return self

    def set_route(self, route: str):
        self.route = route
        return self

    def set_method(self, method: str):
        self.method = method
        return self


class HttpClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.auth = None
        self.__default_headers: dict = {}

    def set_auth(self, auth):
        self.auth = auth
        return self

    def add_default_headers(self, headers: dict):
        for x in headers.keys():
            self.__default_headers[x] = headers[x]

    def send(self, command: HttpCommand) -> Response:
        name = f'_{self.__class__.__name__}__{command.method.lower()}'
        command.auth = self.auth if self is not None else command.auth
        try:
            for x in self.__default_headers.keys():
                command.headers[x] = self.__default_headers[x]
            method_to_call = getattr(self, name)
            return method_to_call(command)
        except Exception as e:
            print(str(e))
            raise e

    def __get(self, command: HttpCommand) -> Response:
        # setup
        url = f'{self.base_url}{command.route}'

        # invoke
        return requests.get(url, auth=self.auth, headers=command.headers)

    def __post(self, command: HttpCommand) -> Response:
        # setup
        url = f'{self.base_url}{command.route}'

        # invoke
        return requests.post(url, json=command.body, auth=self.auth, headers=command.headers)

    def __patch(self, command: HttpCommand) -> Response:
        # setup
        url = f'{self.base_url}{command.route}'

        # invoke
        return requests.patch(url, json=command.body, auth=self.auth, headers=command.headers)
