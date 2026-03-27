from login import login

def test_valid_login():
    assert login("admin", "1234") == "Test Passed"

def test_invalid_login():
    assert login("admin", "wrong") == "Test Failed"
