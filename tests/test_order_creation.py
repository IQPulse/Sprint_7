import pytest
import allure

@allure.feature("Order Creation")
@allure.story("Проверка создания заказов")
class TestOrderCreation:

    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    @allure.title("Test creating order with different colors")
    def test_create_order(self, api_client, color):
        order_data = {
            "firstName": "Anton",
            "lastName": "Nazarov",
            "address": "Moscow, 1",
            "metroStation": 1,
            "phone": "+7 800 100 20 30",
            "rentTime": 5,
            "deliveryDate": "2024-04-08",
            "comment": "Go faster",
            "color": color
        }

        with allure.step(f"Create order with color: {color}"):
            response = api_client.create_order(order_data)
            assert "track" in response.json()
