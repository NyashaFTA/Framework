from dataclasses import dataclass
from faker import Faker
import time

fake = Faker()


@dataclass
class User:
    email: str
    password: str


def generate_user():

    timestamp = int(time.time())

    return User(
        email=f"testuser_{timestamp}@testmail.com",
        password=fake.password(
            length=12, special_chars=True, digits=True, upper_case=True, lower_case=True
        ),
    )
