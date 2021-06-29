from config.api import TestAPI
from infra.http_client import HttpClient, HttpCommand


class WorkPackagesApi:
    def __init__(self, base_url: str):
        self.http_client = HttpClient(base_url)

    # @GET /work_packages/:id
    def get_work_package(self, work_package_id: str):
        command = HttpCommand().set_route(f'/work_packages/{work_package_id}').set_method('GET')
        return self.http_client.send(command)

    # @POST /work_packages/
    def create_work_package(self, body):
        command = HttpCommand().set_route('/work_packages').set_method('POST').set_body(body)
        return self.http_client.send(command)

    # @PATCH /work_packages/:id
    def update_work_package(self, project_id: str, body):
        command = {
            "type": "PATCH",
            "headers": self.headers,
            "auth": self.auth,
            "route": f'/work_packages/{project_id}',
            "body": body
        }
        return self.http_client.get(command)

    # @DELETE /work_packages/:id
    def delete_work_package(self, project_id: str):
        command = {
            "type": "DELETE",
            "headers": self.headers,
            "auth": self.auth,
            "route": f'/work_packages/{project_id}'
        }
        return self.http_client.get(command)
