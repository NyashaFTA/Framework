from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.settings import BASE_URL


class LandingProfilePage(BasePage):
    URL = f"{BASE_URL}/profile"

    SMILEY_BUTTON = (By.CLASS_NAME, "profile-menu")
    SMILEY_BUTTON_DROPDOWN = (By.XPATH, '//div[contains(text(), "Выйти")]')
    # LOGGED_USER_EMAIL = (By.XPATH, '//div[contains(text(), f"{test_user.email}")]')

    def page_is_loaded(self):
        self.driver.current_url = self.URL

