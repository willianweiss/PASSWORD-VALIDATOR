import re


def is_password_valid(password: str) -> bool:
    """
    Validates the password according to the following rules:
    - Nine or more characters
    - At least 1 digit
    - At least 1 lowercase letter
    - At least 1 uppercase letter
    - At least 1 special character: !@#$%^&*()-+
    - No repeated characters
    """

    # Rule 1: Nine or more characters
    if len(password) < 9:
        return False

    # Rule 2: At least 1 digit
    if not re.search(r"\d", password):
        return False

    # Rule 3: At least 1 lowercase letter
    if not re.search(r"[a-z]", password):
        return False

    # Rule 4: At least 1 uppercase letter
    if not re.search(r"[A-Z]", password):
        return False

    # Rule 5: At least 1 special character
    if not re.search(r"[!@#$%^&*()-+]", password):
        return False

    # Rule 6: No repeated characters
    if len(password) != len(set(password)):
        return False

    return True
