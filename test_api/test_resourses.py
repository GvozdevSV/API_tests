import requests


class TestResources:

    def test_get_resource_list(self):
        response = requests.get('https://reqres.in/api/unknown')
        response_json = response.json()

        assert len(response_json['data']) >= 6
        assert response.status_code == 200

    def test_get_single_resource(self):
        response = requests.get('https://reqres.in/api/unknown/3')
        response_json = response.json()

        assert response.status_code == 200
        assert ((response_json['data'])['id']) == 3
