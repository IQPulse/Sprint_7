import pytest
from api.api_client import APIClient

@pytest.fixture(scope="class")
def api_client():
    return APIClient()