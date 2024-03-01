import requests

import Models.users_page
import validator


class TestUsers:

    def test_get_user_list(self):
        response = requests.get('https://reqres.in/api/users?page=2').json()
        assert validator.validator_pydantic(response, Models.users_page.UsersList.Model)

    def test_get_single_user(self):
        response = requests.get('https://reqres.in/api/users/5')
        response_json = response.json()
        f = response_json['data']
        assert response.status_code == 200
        assert f['email'] == 'charles.morris@reqres.in'

    def test_single_user_not_found(self):
        response = requests.get('https://reqres.in/api/users/22')

        assert response.status_code == 404
        assert response.json() == {}

    def test_create_user(self):
        payload = {
            "name": "morpheus",
            "job": "leader"
        }
        response = requests.post('https://reqres.in/api/users', json=payload)

        assert response.status_code == 201
        assert response.json()['name'] == payload['name']

    def test_put_update_user(self):
        payload = {
            "name": "morpheus",
            "job": "zeon leader"
        }
        response = requests.put('https://reqres.in/api/users/2', json=payload)

        assert response.status_code == 200
        assert response.json()['job'] == payload['job']

    def test_patch_update_user(self):
        payload = {
            "name": "morpheus",
            "job": "zeon president"
        }
        response = requests.patch('https://reqres.in/api/users/2', json=payload)

        assert response.status_code == 200
        assert response.json()['job'] == payload['job']

    def test_delete_user(self):
        response = requests.delete('https://reqres.in/api/users/2')
        assert response.status_code == 204
