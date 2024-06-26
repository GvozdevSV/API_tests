import random

import allure
import requests
from endpoints.base_endpoint import BaseEndpoint


class UsersEndpoint(BaseEndpoint):
    response = None
    response_json = None

    @allure.step("Получить список пользователей")
    def get_users_list(self, token=None):
        self.response = requests.get(url=self.users_url, headers=token)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Получить количество пользователей")
    def get_total_users(self):
        return self.response_json['total']

    @allure.step("Получить id пользователя по email")
    def get_users_id_by_email(self, email):
        self.get_users_list()
        users = self.response_json["data"]
        for user in users:
            if user['email'] == email:
                return user['id']

    @allure.step("Получить пользователя по id")
    def get_single_user(self, user_id, token=None):
        self.response = requests.get(url=self.users_url + f'/{user_id}', headers=token)
        self.response_json = self.response.json()
        return self.response_json

    @allure.step("Получить случайного пользователя")
    def get_random_single_user(self, token=None):
        self.get_users_list()
        total_users = self.get_total_users()
        self.get_single_user(random.randint(1, total_users), token)
        return self.response

    @allure.step("Получить ответ об отсутствии пользователя")
    def single_user_not_found(self, token=None):
        self.get_users_list()
        total_users = self.get_total_users()
        self.get_single_user(total_users + 1, token)
        return self.response

    @allure.step("Создание пользователя")
    def create_user(self, payload, token=None):
        self.response = requests.post(url=self.users_url, headers=token, json=payload)
        return self.response

    @allure.step("Перезаписать пользователя")
    def put_user(self, payload, user_id, token=None):
        self.response = requests.put(url=self.users_url + f'/{user_id}', headers=token, json=payload)
        return self.response
