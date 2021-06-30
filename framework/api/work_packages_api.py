from requests import Response
from requests.auth import HTTPBasicAuth
from infra.http_client import HttpClient, HttpCommand


class WorkPackagesApi:
    def __init__(self, base_url: str, api_key: str):
        self.base_route = '/api/v3/work_packages'
        self.http_client = HttpClient(base_url).set_auth(HTTPBasicAuth('apikey', api_key))

    def set_headers(self, headers):
        self.http_client.add_default_headers(headers)
        return self

    def set_auth(self, auth):
        self.http_client.set_auth(auth)
        return self

    # GET /work_packages/:id
    def get_work_package(self, work_package_id: str) -> Response:
        command = HttpCommand().set_route(f'{self.base_route}/{work_package_id}').set_method('GET')
        return self.http_client.send(command)

    # POST /work_packages/
    def create_work_package(self, body):
        command = HttpCommand().set_body(body).set_route(self.base_route).set_method('POST')
        return self.http_client.send(command)

    # PATCH /work_packages/:id
    def update_work_package(self, work_package_id: str, body):
        command = HttpCommand().set_body(body).set_route(f'{self.base_route}/{work_package_id}').set_method('PATCH')
        return self.http_client.send(command)

    # DELETE /work_packages/:id
    def delete_work_package(self, work_package_id: str):
        command = HttpCommand().set_route(f'{self.base_route}/{work_package_id}').set_method('DELETE')
        return self.http_client.send(command)