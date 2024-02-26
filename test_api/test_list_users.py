import requests


class TestUsers:

    def test_get_user_list(self):
        response = requests.get('https://reqres.in/api/users?page=2').json()
        assert response['page'] >= 1
