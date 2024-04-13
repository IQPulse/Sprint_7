import pytest
from api.api_client import APIClient

@pytest.fixture(scope="class")
def api_client():
    return APIClient()


@pytest.fixture(scope="class")
def required_fields(self):
    return ["id", "firstName", "lastName", "address", "metroStation", "phone",
            "rentTime", "deliveryDate", "track", "color", "comment", "createdAt",
            "updatedAt", "status"]