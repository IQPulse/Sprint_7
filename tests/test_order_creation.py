import pytest
from api.api_client import APIClient
import allure

class TestOrderCreation:

    @pytest.fixture(scope="class")
    def order_data(self):
        return {
            "firstName": "Anton",
            "lastName": "Nazarov",
            "address": "Moscow, 1",
            "metroStation": 1,
            "phone": "+7 800 100 20 30",
            "rentTime": 5,
            "deliveryDate": "2024-04-08",
            "comment": "Go faster"
        }

    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    @allure.feature("Order Creation")
    @allure.story("Create Order")
    @allure.title("Test creating order with different colors")
    def test_create_order(self, api_client, order_data, color):
        order_data["color"] = color

        with allure.step(f"Create order with color: {color}"):
            response = api_client.create_order(order_data)
            assert response.status_code == 201, f"Failed to create order with color {color}. Response: {response.text}"
            assert "track" in response.json(), f"No tracking number found in response: {response.json()}"

