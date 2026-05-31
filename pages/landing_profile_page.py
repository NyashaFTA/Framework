from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.environments import BASE_URL


class LandingProfilePage(BasePage):
    URL = f"{BASE_URL}/profile"

    SMILEY_BUTTON = (By.CLASS_NAME, "profile-menu")
    SMILEY_BUTTON_DROPDOWN = (By.XPATH, '//div[contains(text(), "Выйти")]')
    ENTER_PROMOCODE_BUTTON = (By.XPATH, '//div[contains(text(), " Ввести промокод ")]')
    TARIFF_SELECTION_FORM = (By.CLASS_NAME, "profile__tariff")


    def enter_promocode_button_is_visible(self):
        return self.is_visible(self.ENTER_PROMOCODE_BUTTON)

    def tariff_selection_form_is_visible(self):
        return self.is_visible(self.TARIFF_SELECTION_FORM)