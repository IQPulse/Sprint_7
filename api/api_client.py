import requests
import allure
from utils.constants import BASE_URL

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL

    @allure.step("Create courier")
    def create_courier(self, login, password, first_name):
        url = f"{self.base_url}/courier"
        data = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(url, json=data)
        return response

    @allure.step("Delete courier")
    def delete_courier(self, courier_id):
        url = f"{self.base_url}/courier/{courier_id}"
        response = requests.delete(url)
        return response

    @allure.step("Create courier without login or password")
    def create_courier_without_login_or_password(self, data):
        url = f"{self.base_url}/courier"
        response = requests.post(url, json=data)
        return response

    @allure.step("Courier login")
    def courier_login(self, login, password):
        url = f"{self.base_url}/courier/login"
        data = {
            "login": login,
            "password": password
        }
        response = requests.post(url, json=data)
        return response

    @allure.step("Create order")
    def create_order(self, order_data):
        url = f"{self.base_url}/orders"
        response = requests.post(url, json=order_data)
        return response

    @allure.step("Get orders")
    def get_orders(self):
        url = f"{self.base_url}/orders"
        response = requests.get(url)
        return response
