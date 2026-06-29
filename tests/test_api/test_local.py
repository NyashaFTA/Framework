import requests

BASE_URL = "http://127.0.0.1:8000/api/v1"


def user_exists_in_full_user_list():
    user_response = requests.get(f"{BASE_URL}/users/2")
    assert user_response.status_code == 200, (
        f"Не удалось получить пользователя. "
        f"Status code: {user_response.status_code}"
    )

    user = user_response.json()
    print(f"[OK] Получен пользователь: {user}")

    users_response = requests.get(f"{BASE_URL}/users")
    assert users_response.status_code == 200, (
        f"Не удалось получить список пользователей. "
        f"Status code: {users_response.status_code}"
    )

    users = users_response.json()
    print(f"[OK] Получено пользователей: {len(users)}")

    # 3. Проверка
    assert user in users, (
        f"Пользователь с id={user['id']} не найден в списке пользователей"
    )

    print(f"[SUCCESS] Пользователь {user['name']} найден в списке пользователей")