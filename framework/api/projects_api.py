from requests import Response
from requests.auth import HTTPBasicAuth

from infra.http_client import HttpClient, HttpCommand


class ProjectsApi:
    def __init__(self, base_url: str, api_key: str):
        self.base_route = '/api/v3/projects'
        self.http_client = HttpClient(base_url).set_auth(HTTPBasicAuth('apikey', api_key))

    def set_headers(self, headers):
        self.http_client.add_default_headers(headers)
        return self

    def set_auth(self, auth):
        self.http_client.set_auth(auth)
        return self

    # @GET /projects/:id
    def get_project(self, project_id: str) -> Response:
        command = HttpCommand().set_route(f'{self.base_route}/{project_id}')
        return self.http_client.send(command)

    # @POST /projects/
    def create_project(self, body):
        command = HttpCommand().set_body(body).set_route(self.base_route).set_method('POST')
        return self.http_client.send(command)

    # @PATCH /projects/:id
    def update_project(self, project_id: str, body):
        command = HttpCommand().set_body(body).set_route(f'{self.base_route}/{project_id}').set_method('PATCH')
        return self.http_client.send(command)

    # @DELETE /projects/:id
    def delete_project(self, project_id: str):
        command = {
            "type": "DELETE",
            "headers": self.headers,
            "auth": self.auth,
            "route": self.projects_url(project_id)
        }
        return self.http_client.get(command)
