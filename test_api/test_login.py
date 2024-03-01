import requests


class TestLogin:

    def test_successful_login(self):
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        response = requests.post('https://reqres.in/api/login', json=payload)
        assert response.status_code == 200

    def test_unsuccessful_login(self):
        payload = {
            "email": "eve.holt@reqres.in",
        }
        response = requests.post('https://reqres.in/api/login', json=payload)
        assert response.status_code == 400
        assert response.json()['error'] == 'Missing password'
