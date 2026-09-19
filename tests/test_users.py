import pytest
from utils.validators import validate_user_data, validate_create_user_data
from test_data.user_data import VALID_USER 
from test_data.user_data import INVALID_EMAIL_USER
from test_data.user_data import NAME_EMPTY_USER
from test_data.user_data import NAME_MISSING_USER
from test_data.user_data import EMAIL_MISSING_USER
from test_data.user_data import CREATE_USER_CASES

def test_get_users(api_client):
    response = api_client.get("/users")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

    for user in data:
        validate_user_data(user)

def test_create_user(api_client, user_data):

    response = api_client.post("/users",user_data)
    assert response.status_code == 201

    data = response.json()
    validate_user_data(data)
    assert data["name"] == user_data["name"]
    assert data["username"] == user_data["username"]
    assert data["email"] == user_data["email"]

def test_update_user(api_client, user_data):

    response = api_client.put("/users/1", user_data)
    assert response.status_code == 200

    data = response.json()
    validate_user_data(data)

    assert data["name"] == user_data["name"]
    assert data["email"] == user_data["email"]


def test_delete_user(api_client):

    response = api_client.delete("/users/1")
    assert response.status_code == 200 

    data = response.json()
    assert data == {}

def test_get_single_user(api_client):

    response = api_client.get("/users/1")
    assert response.status_code == 200 

    data = response.json()
    validate_user_data(data)

@pytest.mark.parametrize(
    "name, username, email, expected_status",
    [
        ("QA Test", "qa_test", "qa@test.com", 201)
    ]
)
def test_create_user2(
    api_client,
    name,
    username,
    email,
    expected_status,
):
    user_data = {
        "name": name,
        "username": username,
        "email": email
    }

    response = api_client.post("/users", user_data)

    assert response.status_code == expected_status

    data = response.json()

    validate_user_data(data)

    assert data["name"] == name
    assert data["username"] == username
    assert data["email"] == email

@pytest.mark.parametrize(
    "name, email",
    [
        ("QA Test", "qa@test.com"),
        ("QA Tester", "tester@test.com"),
        ("Automation QA", "automation@test.com")
    ]
)

def test_different_data(
    api_client,
    valid_user_data,
    name,
    email
):
    user_data = valid_user_data.copy()
    user_data["name"] = name 
    user_data["email"] = email

    response = api_client.post("/users", user_data)

    assert response.status_code == 201

    data = response.json()

    validate_user_data(data)

    assert data["name"] == name
    assert data["email"] == email

def test_data_import():
    print(VALID_USER)

    assert VALID_USER["name"] == "QA Test"

@pytest.mark.parametrize(
    "user_data, expected_status, expected_result, expected_message",
    CREATE_USER_CASES
)

def test_create_user_cases(
    api_client, 
    user_data, 
    expected_status, 
    expected_result, 
    expected_message
    ):

    user_data = user_data.copy()

    response = api_client.post("/users", user_data)

    assert response.status_code == expected_status

    data = response.json()
    result, message = validate_create_user_data(user_data)

    assert result == expected_result
    assert message == expected_message

    if expected_result :
        assert data["name"] == user_data["name"]
        assert data["email"] == user_data["email"]


def test_create_user_response(api_client, user_data):

    response = api_client.post("/users", json=user_data)
    assert response.status_code == 201
    create_user = response.json()

    assert "id" in create_user 
    assert create_user["name"] == user_data["name"]
    assert create_user["email"] == user_data["email"]
    assert 1 == 2