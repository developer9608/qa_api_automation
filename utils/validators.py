import re

def validate_create_user_data(user):
    if not isinstance(user, dict):
        return (False, "user is not dict type")

    if "name" not in user:
        return (False, "name is missing")
    if "email" not in user:
        return (False, "email is missing")
    if not isinstance(user["name"], str):
        return (False, "invalid name type")
    if not isinstance(user["email"], str):
        return (False, "invalid email type")
    if user["name"].strip() == "":
        return (False, "name is empty")    
    if not re.fullmatch(
        r"[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Za-z0-9]+",
        user["email"].strip()):
        return (False, "invalid email format")
    return (True, None)

def validate_user_data(user):
    if "id" not in user:
        return (False, "id is missing")
    if not isinstance(user["id"], int):
        return (False, "invalid id type")

    if "name" not in user:
        return (False, "name is missing")
    if "email" not in user:
        return (False, "email is missing")
    if not isinstance(user["name"], str):
        return (False, "invalid name type")
    if not isinstance(user["email"], str):
        return (False, "invalid email type")
    if user["name"].strip() == "":
        return (False, "name is empty")    
    if not re.fullmatch(
        r"[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Za-z0-9]+",
        user["email"].strip()):
        return (False, "invalid email format")
    return (True, None)