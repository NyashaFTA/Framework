from core.waits.wait_manager import WaitManager



class BasePage:

    def __init__(
            self,
            driver
    ):

        self.driver = driver

    def click_button(
            self,
            locator
    ):

        element = WaitManager.clickable(
            self.driver,
            locator
        )

        element.click()

    def type(
            self,
            locator,
            text
    ):

        element = WaitManager.visible(
            self.driver,
            locator
        )

        element.clear()

        element.send_keys(
            text
        )

    def get_text(
            self,
            locator
    ):

        element = WaitManager.visible(
            self.driver,
            locator
        )

        return element.text

    def is_visible(
            self,
            locator
    ):

        WaitManager.visible(
            self.driver,
            locator
        )

        return True

    def go_to(
            self,
            url
    ):

        self.driver.get(
            url
        )