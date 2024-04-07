import allure
from utils.helpers import register_new_courier_and_return_login_password

@allure.feature("Courier Login")
@allure.story("Проверка авторизации курьеров")
class TestCourierLogin:

    login_existing = "anton_nazarov_6_1"
    login_error = "anton_nazarov_6"
    password = "qw123!"
    password_error = "qw123!ZXC"

    @allure.title("Test Courier Login Successfully")
    def test_courier_login_successfully(self, api_client):
        new_courier_info = register_new_courier_and_return_login_password()
        login, password, first_name = new_courier_info[0], new_courier_info[1], new_courier_info[2]

        response = api_client.courier_login(login, password)
        assert response.status_code == 200 and "id" in response.json()

        delete_response = api_client.delete_courier(response.json()["id"])

    @allure.title("Test Courier Login Error: Invalid Login")
    def test_courier_login_error_login(self, api_client):
        response = api_client.courier_login(self.login_error, self.password)
        expected_error_message = "Учетная запись не найдена"
        assert response.status_code == 404 and response.json()["message"] == expected_error_message

    @allure.title("Test Courier Login Error: Invalid Password")
    def test_courier_login_error_password(self, api_client):
        response = api_client.courier_login(self.login_existing, self.password_error)
        expected_error_message = "Учетная запись не найдена"
        assert response.status_code == 404 and response.json()["message"] == expected_error_message

    @allure.title("Test Courier Login Error: Missing Login and Password")
    def test_courier_login_missing_login_and_password(self, api_client):
        response = api_client.courier_login("", "")
        expected_error_message = "Недостаточно данных для входа"
        assert response.status_code == 400 and response.json()["message"] == expected_error_message

    @allure.title("Test Courier Login Error: Missing Login")
    def test_courier_login_missing_login(self, api_client):
        response = api_client.courier_login("", self.password)
        expected_error_message = "Недостаточно данных для входа"
        assert response.status_code == 400 and response.json()["message"] == expected_error_message

    @allure.title("Test Courier Login Error: Missing Password")
    def test_courier_login_missing_password(self, api_client):
        response = api_client.courier_login(self.login_existing, "")
        expected_error_message = "Недостаточно данных для входа"
        assert response.status_code == 400 and response.json()["message"] == expected_error_message
