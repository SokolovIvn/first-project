import pytest
import random


@pytest.fixture()
def generate_name():
    name = f"Name{random.randint(100, 999)}"
    return name

@pytest.fixture()
def generate_password():
    pswd = str(random.randint(100000, 999999))
    return pswd

@pytest.fixture()
def get_fixture_email():
    return "testtest@yy.ru"


@pytest.fixture()
def get_fixture_pswd():
    return "123456"

