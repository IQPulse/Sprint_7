import allure


@allure.feature("Order List")
@allure.story("Проверка списка заказов")
class TestOrderList:

    @allure.title("Check presence of required fields in orders")
    def test_get_orders(self, api_client):
        required_fields = ["id", "firstName", "lastName", "address", "metroStation", "phone",
                           "rentTime", "deliveryDate", "track", "color", "comment", "createdAt",
                           "updatedAt", "status"]

        with allure.step("Send request to retrieve orders"):
            response = api_client.get_orders()
            orders = response.json().get("orders", [])

        with allure.step("Check presence of required fields"):
            missing_fields = [field for field in required_fields if field not in orders[0]]
            assert not missing_fields
