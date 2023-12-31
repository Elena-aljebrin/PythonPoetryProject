import pytest
from project import code


def test_code():
    assert code.is_acceptable_password("short") == False
    assert code.is_acceptable_password("short54") == True
    assert code.is_acceptable_password("muchlonger") == True
    assert code.is_acceptable_password("ashort") == False
    assert code.is_acceptable_password("muchlonger5") == True
    assert code.is_acceptable_password("sh5") == False
    assert code.is_acceptable_password("1234567") == False
    assert code.is_acceptable_password("12345678910") == True
    assert code.is_acceptable_password("password12345") == False
    assert code.is_acceptable_password("PASSWORD12345") == False
    assert code.is_acceptable_password("pass1234word") == True
    assert code.is_acceptable_password("aaaaaa1") == False
    assert code.is_acceptable_password("aaaaaabbbbb") == False
    assert code.is_acceptable_password("aaaaaabb1") == True
    assert code.is_acceptable_password("abc1") == False
    assert code.is_acceptable_password("abbcc12") == True
    assert code.is_acceptable_password("aaaaaaabbaaaaaaaab") == False
