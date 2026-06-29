import requests
#import logging
from models.models import (
    CreateUserRequest,
    UpdateUserRequest,
)

#logger = logging.getLogger(__name__)

#def test_get_users(api):
#
#    users = api.get_users()
#
#    assert len(users) > 0
#
#    assert users[0].id > 0
#
#    assert users[0].is_active is True

def test_create_user(api, test_api_user):

    request = CreateUserRequest(
        name=test_api_user.name,
        email=test_api_user.email,
        is_active=test_api_user.is_active
    )

    created = api.create_user(request)

    assert created.name == request.name

    assert created.email == request.email

    assert created.is_active is True


def test_update_user(api):

    request = UpdateUserRequest(
        name="Updated",
        email="updated@test.com",
        is_active=False
    )

    updated = api.update_user(
        1,
        request
    )

    assert updated.name == request.name

    assert updated.email == request.email

    assert updated.is_active is False


def test_delete_user(api):

    api.delete_user(1)

    response = requests.get(
        "http://localhost:8000/users/1"
    )

    assert response.status_code == 404