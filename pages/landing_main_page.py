from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LandingMainPage(BasePage):

    URL = "https://test.pstv.ru/"

    TORSO_BUTTON = (By.CLASS_NAME, 'auth-button')
    AUTHRORIZATION_MODAL = (By.CLASS_NAME, 'authorization')
    AUTH_BY_EMAIL_BUTTON = (By.CLASS_NAME, 'authorization__email-button')
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[inputmode="email"]')
    PASSWORD_FIELD = (By.ID, 'id-single-factor-code-text-field')