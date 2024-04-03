import pytest
import allure
import requests
from utils.constants import GET_LOGIN_URL
from utils.helpers import register_new_courier_and_return_login_password
from api.api_client import APIClient

class TestCourierCreation:
    login_suffix = "10000001000"
    login_existing = "anton_nazarov_6_1"
    password = "qw123!"
    first_name = "Anton"

    @pytest.fixture(scope="class")
    def api_client(self):
        return APIClient()

    @allure.feature("Courier Creation")
    @allure.story("Successful Creation")
    def test_create_courier_answer_201_and_ok(self, api_client):
        allure.dynamic.title("Test Create Courier: Answer 201 and OK")
        new_courier_info = register_new_courier_and_return_login_password()
        login, password, first_name = new_courier_info[0][:-1], new_courier_info[1], new_courier_info[2]

        response = api_client.create_courier(login, password, first_name)
        assert response.status_code == 201 and response.json()["ok"]

        get_id_data = {
            "login": login,
            "password": password
        }
        get_id_response = requests.post(GET_LOGIN_URL, json=get_id_data)

        courier_id = get_id_response.json().get("id")

        delete_response = api_client.delete_courier(courier_id)

    @allure.feature("Courier Creation")
    @allure.story("Successful Creation")
    def test_create_courier_answer_ok_true(self, api_client):
        allure.dynamic.title("Test Create Courier: Answer OK True")
        new_courier_info = register_new_courier_and_return_login_password()
        login, password, first_name = new_courier_info[0][:-1], new_courier_info[1], new_courier_info[2]

        response = api_client.create_courier(login, password, first_name)
        assert response.status_code == 201 and response.json()["ok"] == True

        get_id_data = {
            "login": login,
            "password": password
        }
        get_id_response = requests.post(GET_LOGIN_URL, json=get_id_data)

        courier_id = get_id_response.json().get("id")

        delete_response = api_client.delete_courier(courier_id)

    @allure.feature("Courier Creation")
    @allure.story("Conflict on Creation")
    def test_create_courier_double(self, api_client):
        allure.dynamic.title("Test Create Courier: Conflict on Creation")
        new_courier_info = register_new_courier_and_return_login_password()
        login, password, first_name = new_courier_info[0][:-1], new_courier_info[1], new_courier_info[2]

        response1 = api_client.create_courier(login, password, first_name)

        response2 = api_client.create_courier(login, password, first_name)

        expected_message = "Этот логин уже используется. Попробуйте другой."
        assert response2.status_code == 409 and expected_message in response2.json()["message"]

        if response1.status_code == 201:
            get_id_data = {
                "login": login,
                "password": password
            }
            get_id_response = requests.post(GET_LOGIN_URL, json=get_id_data)
            courier_id = get_id_response.json().get("id")
            delete_response = api_client.delete_courier(courier_id)

    @allure.feature("Courier Creation")
    @allure.story("Error Handling")
    def test_create_courier_missing_login(self, api_client):
        allure.dynamic.title("Test Create Courier: Missing Login")
        payload = {
            "password": self.password,
            "firstName": self.first_name
        }
        response = api_client.create_courier_without_login_or_password(payload)

        expected_message = "Недостаточно данных для создания учетной записи"
        assert response.status_code == 400 and expected_message in response.json()["message"]

    @allure.feature("Courier Creation")
    @allure.story("Error Handling")
    def test_create_courier_missing_password(self, api_client):
        allure.dynamic.title("Test Create Courier: Missing Password")
        login = self.login_existing

        payload = {
            "login": login,
            "firstName": self.first_name
        }
        response = api_client.create_courier_without_login_or_password(payload)

        expected_message = "Недостаточно данных для создания учетной записи"
        assert response.status_code == 400 and expected_message in response.json()["message"]

    @allure.feature("Courier Creation")
    @allure.story("Error Handling")
    def test_create_existing_login_courier_error(self, api_client):
        allure.dynamic.title("Test Create Courier: Existing Login Error")
        login = self.login_existing
        password = self.password

        response = api_client.create_courier(login, password, self.first_name)

        expected_error_message = "Этот логин уже используется. Попробуйте другой."
        assert response.status_code == 409 and response.json()["message"] == expected_error_message