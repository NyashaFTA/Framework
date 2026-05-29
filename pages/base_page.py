import logging
from selenium.common.exceptions import TimeoutException
from core.waits.wait_manager import WaitManager
import time
from selenium.webdriver.common.action_chains import ActionChains


logger = logging.getLogger(__name__)


class BasePage:
    def __init__(self, driver):

        self.driver = driver

    def find(self, locator):

        logger.info(f"Find element: {locator}")

        return WaitManager.present(self.driver, locator)

    def click_button(self, locator):

        logger.info(f"Click: {locator}")

        element = WaitManager.clickable(self.driver, locator)

        element.click()

    def type(self, locator, text):

        logger.info(f"Typing text into: {locator}")

        element = WaitManager.visible(self.driver, locator)

        element.clear()

        element.send_keys(text)

    def get_text(self, locator):

        logger.info(f"Get text: {locator}")

        element = WaitManager.visible(self.driver, locator)

        return element.text

    def is_visible(self, locator):

        try:
            WaitManager.visible(self.driver, locator)

            return True

        except TimeoutException:
            return False

    def is_present(self, locator):

        try:
            WaitManager.present(self.driver, locator)

            return True

        except TimeoutException:
            return False

    def go_to(self, url):

        logger.info(f"Open page: {url}")

        self.driver.get(url)

    def refresh(self):

        logger.info("Refresh page")

        self.driver.refresh()

    def scroll_to_element(self, locator):

        logger.info(f"Scroll to: {locator}")

        element = WaitManager.present(self.driver, locator)

        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def type_otp_code(self, locator, text):
        
        logger.info(f"Typing OTP code into: {locator}")

        first_field = WaitManager.visible(self.driver, locator)
        first_field.click()
        first_field.clear()

        actions = ActionChains(self.driver)
        for digit in str(text):
            actions.send_keys(digit)
            actions.perform()
            time.sleep(0.1)

    
