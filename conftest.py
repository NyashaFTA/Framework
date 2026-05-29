import pytest
from utils.user_generator import generate_user
import os
import logging
import logging.config
from core.browser.driver_factory import DriverFactory
from core.browser.browser_config import BrowserConfig
from core.browser.browser_type import BrowserType

os.makedirs("logs", exist_ok=True)

logging.config.fileConfig("config/logging.ini", disable_existing_loggers=False)

logger = logging.getLogger(__name__)


def pytest_addoption(parser):

    parser.addoption("--browser", default="chrome")

    parser.addoption("--mobile", action="store_true")

    parser.addoption("--headless", action="store_true")


@pytest.fixture
def driver(request):

    logger.info("Creating browser configuration")

    config = BrowserConfig(
        browser=BrowserType(request.config.getoption("--browser")),
        mobile=request.config.getoption("--mobile"),
        headless=request.config.getoption("--headless"),
    )

    logger.info(
        f"Browser={config.browser} | "
        f"Headless={config.headless} | "
        f"Mobile={config.mobile}"
    )

    logger.info("Starting browser session")

    driver = DriverFactory.create_driver(config)

    yield driver

    logger.info("Closing browser session")

    DriverFactory.quit_driver(driver)


@pytest.fixture
def test_user():

    logger.info("Generating test user")

    return generate_user()


@pytest.fixture
def valid_auth_code():

    logger.info("Reading AUTH_CODE")

    auth_code = os.getenv("AUTH_CODE")

    if not auth_code:
        logger.error("AUTH_CODE not found")

        pytest.fail("Не найден валидный код авторизации")

    return auth_code
