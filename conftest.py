import pytest
from utils.user_generator import generate_user
import os


from core.browser.driver_factory import (
    DriverFactory
)

from core.browser.browser_config import (
    BrowserConfig
)

from core.browser.browser_type import (
    BrowserType
)


def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        default="chrome"
    )

    parser.addoption(
        "--mobile",
        action="store_true"
    )

    parser.addoption(
        "--headless",
        action="store_true"
    )


@pytest.fixture
def driver(request):

    config = BrowserConfig(

        browser=BrowserType(
            request.config.getoption(
                "--browser"
            )
        ),

        mobile=request.config.getoption(
            "--mobile"
        ),

        headless=request.config.getoption(
            "--headless"
        )
    )

    driver = DriverFactory.create_driver(
        config
    )

    yield driver

    driver.quit()

@pytest.fixture
def test_user():

    return generate_user()

@pytest.fixture
def valid_auth_code():
    auth_code = os.getenv("AUTH_CODE")
    if not auth_code:
        pytest.fail("Не найден валидный код авторизации")

    return(auth_code)