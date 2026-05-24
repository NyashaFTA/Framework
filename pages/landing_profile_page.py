from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LandingProfilePage(BasePage):

    URL = "https://test.pstv.ru/profile"

    SMILEY_BUTTON = (By.CLASS_NAME, 'profile-menu')
    SMILEY_BUTTON_DROPDOWN = (By.XPATH, '//div[contains(text(), "Выйти")]')
    LOGGED_USER_EMAIL = (By.XPATH, '//div[contains(text(), f"{test_user.email}")]')
    

