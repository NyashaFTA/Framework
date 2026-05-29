import logging

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
)

from config.settings import EXPLICIT_WAIT, POLL_FREQUENCY


logger = logging.getLogger(__name__)


class WaitManager:
    IGNORED_EXCEPTIONS = (NoSuchElementException, StaleElementReferenceException)

    @staticmethod
    def _wait(driver, timeout=EXPLICIT_WAIT):

        return WebDriverWait(
            driver=driver,
            timeout=timeout,
            poll_frequency=POLL_FREQUENCY,
            ignored_exceptions=WaitManager.IGNORED_EXCEPTIONS,
        )

    @staticmethod
    def visible(driver, locator, timeout=EXPLICIT_WAIT):

        logger.info(f"Waiting visible: {locator}")

        return WaitManager._wait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @staticmethod
    def clickable(driver, locator, timeout=EXPLICIT_WAIT):

        logger.info(f"Waiting clickable: {locator}")

        return WaitManager._wait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @staticmethod
    def present(driver, locator, timeout=EXPLICIT_WAIT):

        logger.info(f"Waiting present: {locator}")

        return WaitManager._wait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @staticmethod
    def invisible(driver, locator, timeout=EXPLICIT_WAIT):

        logger.info(f"Waiting invisible: {locator}")

        return WaitManager._wait(driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @staticmethod
    def all_visible(driver, locator, timeout=EXPLICIT_WAIT):

        logger.info(f"Waiting all visible: {locator}")

        return WaitManager._wait(driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )
