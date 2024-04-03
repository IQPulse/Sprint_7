import pytest
from api.api_client import APIClient
import allure


class TestOrderList:
    @pytest.fixture(scope="class")
    def api_client(self):
        return APIClient()

    @pytest.fixture(scope="class")
    def required_fields(self):
        return ["id", "firstName", "lastName", "address", "metroStation", "phone",
                "rentTime", "deliveryDate", "track", "color", "comment", "createdAt",
                "updatedAt", "status"]

    @allure.feature("Order List")
    @allure.story("Retrieving Orders")
    @allure.title("Check presence of required fields in orders")
    def test_get_orders(self, api_client, required_fields):
        with allure.step("Send request to retrieve orders"):
            response = api_client.get_orders()
            orders = response.json().get("orders", [])

        with allure.step("Check presence of required fields"):
            assert all(field in order for field in required_fields for order in orders), \
                f"One or more required fields missing in orders: {required_fields}"

