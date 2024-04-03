import requests
from utils.constants import BASE_URL

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL

    def create_courier(self, login, password, first_name):
        url = f"{self.base_url}/courier"
        data = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(url, json=data)
        return response

    def delete_courier(self, courier_id):
        url = f"{self.base_url}/courier/{courier_id}"
        response = requests.delete(url)
        return response

    def create_courier_without_login_or_password(self, data):
        url = f"{self.base_url}/courier"
        response = requests.post(url, json=data)
        return response

    def courier_login(self, login, password):
        url = f"{self.base_url}/courier/login"
        data = {
            "login": login,
            "password": password
        }
        response = requests.post(url, json=data)
        return response

    def create_order(self, order_data):
        url = f"{self.base_url}/orders"
        response = requests.post(url, json=order_data)
        return response

    def get_orders(self):
        url = f"{self.base_url}/orders"
        response = requests.get(url)
        return response