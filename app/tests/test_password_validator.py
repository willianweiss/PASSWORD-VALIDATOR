from app.services.password_validator import is_password_valid


def test_password_valid():
    assert is_password_valid("AbTp9!fok") == True


def test_password_invalid():
    assert is_password_valid("") == False
    assert is_password_valid("aa") == False
    assert is_password_valid("ab") == False
    assert is_password_valid("AAAbbbCc") == False
    assert is_password_valid("AbTp9!foo") == False
    assert is_password_valid("AbTp9!foA") == False
    assert is_password_valid("AbTp9 fok") == False
