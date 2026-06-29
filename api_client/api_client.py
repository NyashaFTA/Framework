import requests

from models.models import (
    User,
    CreateUserRequest,
    UpdateUserRequest,
)

from pydantic import TypeAdapter


class UserApi:

    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_users(self) -> list[User]:
        response = requests.get(f"{self.base_url}/users")

        assert response.status_code == 200

        return TypeAdapter(list[User]).validate_python(
            response.json()
        )

    def get_user(self, user_id: int) -> User:
        response = requests.get(
            f"{self.base_url}/users/{user_id}"
        )

        assert response.status_code == 200

        return User.model_validate(response.json())

    def create_user(
            self,
            request: CreateUserRequest
    ) -> User:

        response = requests.post(
            f"{self.base_url}/users",
            json=request.model_dump()
        )

        assert response.status_code == 201

        return User.model_validate(response.json())

    def update_user(
            self,
            user_id: int,
            request: UpdateUserRequest
    ) -> User:

        response = requests.put(
            f"{self.base_url}/users/{user_id}",
            json=request.model_dump()
        )

        assert response.status_code == 200

        return User.model_validate(response.json())

    def delete_user(self, user_id: int):

        response = requests.delete(
            f"{self.base_url}/users/{user_id}"
        )

        assert response.status_code == 204