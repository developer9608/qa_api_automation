import requests

class ApiClient:

    def __init__(self,base_url):
        self.base_url = base_url

    def get(self, path):
        url = f"{self.base_url}{path}"
        response = requests.get(url)
        return response

    def post(self, endpoint, json):
        return requests.post(
            f"{self.base_url}{endpoint}",
            json=json
        )

    def put(self, endpoint, json):
        return requests.put(
            f"{self.base_url}{endpoint}",
            json=json
        )

    def delete(self, endpoint):
        return requests.delete(
            f"{self.base_url}{endpoint}"
        )