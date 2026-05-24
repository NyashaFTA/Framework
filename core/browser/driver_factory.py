from selenium import webdriver

from core.browser.browser_type import BrowserType


class DriverFactory:

    @staticmethod
    def create_driver(config):

        if config.browser == BrowserType.CHROME:

            options = webdriver.ChromeOptions()

            if config.mobile:

                options.add_experimental_option(
                    "mobileEmulation",
                    {
                        "deviceName": "iPhone 14 Pro"
                    }
                )

            if config.headless:

                options.add_argument(
                    "--headless=new"
                )

            options.add_argument(
                "--start-maximized"
            )

            return webdriver.Chrome(
                options=options
            )

        if config.browser == BrowserType.FIREFOX:

            options = webdriver.FirefoxOptions()

            if config.headless:

                options.add_argument(
                    "--headless"
                )

            driver = webdriver.Firefox(
                options=options
            )

            if config.mobile:

                driver.set_window_size(
                    390,
                    844
                )

            return driver

        if config.browser == BrowserType.SAFARI:

            return webdriver.Safari()

        raise ValueError(
            f"Unsupported browser "
            f"{config.browser}"
        )