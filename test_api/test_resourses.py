import requests


class TestResources:

    def test_get_resource_list(self):
        response = requests.get('https://reqres.in/api/unknown')
        response_json = response.json()

        assert len(response_json['data']) >= 6
        assert response.status_code == 200