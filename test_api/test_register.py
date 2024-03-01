import requests


class TestRegister:

    def test_successful_register(self):
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        response = requests.post('https://reqres.in/api/register', json=payload)
        assert response.status_code == 200
