from dataclasses import dataclass
from faker import Faker
import time

fake = Faker()


@dataclass
class User:
    email: str
    password: str

@dataclass
class APIuser:
    name: str
    email: str
    is_active: int

def generate_user():

    timestamp = int(time.time())

    return User(
        email=f"testuser_{timestamp}@testmail.com",
        password=fake.password(
            length=12, special_chars=True, digits=True, upper_case=True, lower_case=True
        ),
    )

def generate_api_user():

    timestamp = int(time.time())

    return APIuser(
        name=fake.name(),
        email=f"testapiuser_{timestamp}@testmail.com",
        is_active=fake.pybool()
    )