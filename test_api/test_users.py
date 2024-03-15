from datetime import datetime, timedelta

import requests

from models.users_model import UsersList, SingleUser, RequestUser, ResponseCreateUser, ResponsePutUser
from test_api.base_test import BaseTest
from validator import validator_pydantic


class TestUsers(BaseTest):

    def test_get_user_list(self):
        response = self.user_endpoint.get_users_list()

        assert response.status_code == 200
        assert validator_pydantic(response.json(), UsersList.Model)

    def test_get_single_user(self):
        response = self.user_endpoint.get_random_single_user()

        assert response.status_code == 200
        assert validator_pydantic(response.json(), SingleUser.Model)

    def test_single_user_not_found(self):
        response = self.user_endpoint.single_user_not_found()

        assert response.status_code == 404
        assert response.json() == {}

    def test_create_user(self):
        payload = RequestUser.Model().model_dump()
        response = self.user_endpoint.create_user(payload=payload)

        assert response.status_code == 201
        assert response.json()['name'] == payload['name']
        assert validator_pydantic(response.json(), ResponseCreateUser.Model)

    def test_put_update_user(self):
        payload = RequestUser.Model(
            job="zeon leader"
        ).model_dump()
        response = self.user_endpoint.put_user(
            payload=payload,
            user_id=2
        )
        assert response.status_code == 200
        assert response.json()['job'] == payload['job']
        assert validator_pydantic(response.json(), ResponsePutUser.Model)

    def test_patch_update_user(self):
        payload = {
            "name": "morpheus",
            "job": "zeon leader"
        }
        response = requests.patch('https://reqres.in/api/users/2', json=payload)
        print(response.json())

        assert response.status_code == 200
        assert response.json()['job'] == payload['job']

    def test_delete_user(self):
        response = requests.delete('https://reqres.in/api/users/2')
        assert response.status_code == 204


