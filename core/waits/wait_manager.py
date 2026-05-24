from selenium.webdriver.support.ui import (
    WebDriverWait
)

from selenium.webdriver.support import (
    expected_conditions as EC
)


class WaitManager:

    DEFAULT_TIMEOUT = 10

    @staticmethod
    def visible(
            driver,
            locator,
            timeout=DEFAULT_TIMEOUT
    ):

        return WebDriverWait(
            driver,
            timeout
        ).until(
            EC.visibility_of_element_located(
                locator
            )
        )

    @staticmethod
    def clickable(
            driver,
            locator,
            timeout=DEFAULT_TIMEOUT
    ):

        return WebDriverWait(
            driver,
            timeout
        ).until(
            EC.element_to_be_clickable(
                locator
            )
        )

    @staticmethod
    def present(
            driver,
            locator,
            timeout=DEFAULT_TIMEOUT
    ):

        return WebDriverWait(
            driver,
            timeout
        ).until(
            EC.presence_of_element_located(
                locator
            )
        )

    @staticmethod
    def invisible(
            driver,
            locator,
            timeout=DEFAULT_TIMEOUT
    ):

        return WebDriverWait(
            driver,
            timeout
        ).until(
            EC.invisibility_of_element_located(
                locator
            )
        )