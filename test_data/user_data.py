import pytest

VALID_USER = {
    "name": "QA Test",
    "username": "qa_test",
    "email": "qa@example.com"
}

INVALID_EMAIL_USER = {
    "name": "QA Test",
    "username": "qa_test",
    "email": "qa_test"
}

NAME_EMPTY_USER = {
    "name": "",
    "username": "qa_test",
    "email": "qa@example.com"
}

NAME_MISSING_USER = {
    "username": "qa_test",
    "email": "qa@example.com"
}

EMAIL_MISSING_USER = {
    "name": "QA TEST",
    "username": "qa_test"
}

CREATE_USER_CASES = [
    pytest.param(
        VALID_USER,
        201,
        True,
        None,
        id="valid_user"
    ),
    pytest.param(
        INVALID_EMAIL_USER,
        201,
        False,
        "invalid email format",
        id="invalid_email"
    ),    
    pytest.param(
        NAME_EMPTY_USER,
        201,
        False,
        "name is empty",
        id="name_empty"
    ),   
    pytest.param(
        NAME_MISSING_USER,
        201,
        False,
        "name is missing",
        id="name_missing"
    ),     
    pytest.param(
        EMAIL_MISSING_USER,
        201,
        False,
        "email is missing",
        id="email_missing"
    ),  
]