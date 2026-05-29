from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from core.browser.browser_type import BrowserType

import logging

logger = logging.getLogger(__name__)


class DriverFactory:
    @staticmethod
    def create_driver(config):

        browser = config.browser

        logger.info(f"Starting browser: {browser}")

        if browser == BrowserType.CHROME:
            return DriverFactory._create_chrome(config)

        if browser == BrowserType.FIREFOX:
            return DriverFactory._create_firefox(config)

        if browser == BrowserType.SAFARI:
            return DriverFactory._create_safari(config)

        raise ValueError(f"Unsupported browser: {browser}")

    @staticmethod
    def _create_chrome(config):

        options = webdriver.ChromeOptions()

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        if config.headless:
            options.add_argument("--headless=new")

        if config.mobile:
            options.add_experimental_option(
                "mobileEmulation", {"deviceName": "iPhone 14 Pro"}
            )

        options.add_argument("--start-maximized")

        driver = webdriver.Chrome(service=ChromeService(), options=options)

        logger.info(
            f"Chrome started | headless={config.headless} | mobile={config.mobile}"
        )

        return driver

    @staticmethod
    def _create_firefox(config):

        options = webdriver.FirefoxOptions()

        if config.headless:
            options.add_argument("--headless")

        driver = webdriver.Firefox(service=FirefoxService(), options=options)

        if config.mobile:
            driver.set_window_size(390, 844)

        logger.info(
            f"Firefox started | headless={config.headless} | mobile={config.mobile}"
        )

        return driver

    @staticmethod
    def _create_safari(config):

        logger.info("Safari started")

        return webdriver.Safari()

    @staticmethod
    def quit_driver(driver):

        if driver:
            logger.info("Closing browser")

            driver.quit()
