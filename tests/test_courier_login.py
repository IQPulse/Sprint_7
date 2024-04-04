from utils.helpers import register_new_courier_and_return_login_password
import allure


class TestCourierLogin:
    login_suffix = "10000001000"
    login_existing = "anton_nazarov_6_1"
    login_error = "anton_nazarov_6"
    password = "qw123!"
    password_error = "qw123!ZXC"
    first_name = "Anton"

    @allure.feature("Courier Login")
    @allure.story("Successful Login")
    def test_courier_login_successfully(self, api_client):
        allure.dynamic.title("Test Courier Login Successfully")
        new_courier_info = register_new_courier_and_return_login_password()
        login, password, first_name = new_courier_info[0], new_courier_info[1], new_courier_info[2]

        response = api_client.courier_login(login, password)
        assert response.status_code == 200 and "id" in response.json()

        delete_response = api_client.delete_courier(response.json()["id"])

    @allure.feature("Courier Login")
    @allure.story("Login Errors")
    def test_courier_login_error_login(self, api_client):
        allure.dynamic.title("Test Courier Login Error: Invalid Login")
        response = api_client.courier_login(self.login_error, self.password)

        expected_error_message = "Учетная запись не найдена"
        assert response.status_code == 404 and response.json()["message"] == expected_error_message

    @allure.feature("Courier Login")
    @allure.story("Login Errors")
    def test_courier_login_error_password(self, api_client):
        allure.dynamic.title("Test Courier Login Error: Invalid Password")
        response = api_client.courier_login(self.login_existing, self.password_error)

        expected_error_message = "Учетная запись не найдена"
        assert response.status_code == 404 and response.json()["message"] == expected_error_message

    @allure.feature("Courier Login")
    @allure.story("Login Errors")
    def test_courier_login_non_existing_user(self, api_client):
        allure.dynamic.title("Test Courier Login Error: Non-existing User")
        response = api_client.courier_login(self.login_error, self.password_error)

        expected_error_message = "Учетная запись не найдена"
        assert response.status_code == 404 and response.json()["message"] == expected_error_message

    @allure.feature("Courier Login")
    @allure.story("Login Errors")
    def test_courier_login_missing_login_and_password(self, api_client):
        allure.dynamic.title("Test Courier Login Error: Missing Login and Password")
        response = api_client.courier_login("","")

        expected_error_message = "Недостаточно данных для входа"
        assert response.status_code == 400 and response.json()["message"] == expected_error_message

    @allure.feature("Courier Login")
    @allure.story("Login Errors")
    def test_courier_login_missing_login(self, api_client):
        allure.dynamic.title("Test Courier Login Error: Missing Login")
        response = api_client.courier_login("", self.password)

        expected_error_message = "Недостаточно данных для входа"
        assert response.status_code == 400 and response.json()["message"] == expected_error_message

    @allure.feature("Courier Login")
    @allure.story("Login Errors")
    def test_courier_login_missing_password(self, api_client):
        allure.dynamic.title("Test Courier Login Error: Missing Password")
        response = api_client.courier_login(self.login_existing, "")

        expected_error_message = "Недостаточно данных для входа"
        assert response.status_code == 400 and response.json()["message"] == expected_error_message
