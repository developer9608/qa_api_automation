import pytest
from api_client import ApiClient
from test_data.user_data import VALID_USER
from config import BASE_URL

@pytest.fixture
def api_client():
    return ApiClient(BASE_URL)

@pytest.fixture
def user_data():
    data = {
        "name": "QA_Test",
        "username": "qa_test",
        "email": "qa@example.com"
    }
    return data

@pytest.fixture
def valid_user_data():
    return VALID_USER.copy()