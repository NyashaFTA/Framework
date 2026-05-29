from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.settings import BASE_URL
from config.settings import AUTH_CODE

class LandingMainPage(BasePage):
    URL = BASE_URL

    TORSO_BUTTON = (By.CLASS_NAME, "auth-button")
    AUTHORIZATION_MODAL = (By.CLASS_NAME, "authorization")
    AUTH_BY_EMAIL_BUTTON = (By.CLASS_NAME, "authorization__email-button")
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[inputmode="email"]')
    AUTH_CODE_FIELD = (By.ID, "id-single-factor-code-text-field")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")

    def open_page(self):
        self.go_to(self.URL)

    def open_authorization_modal(self):
        self.click_button(self.TORSO_BUTTON)

    def select_auth_by_email(self):
        self.click_button(self.AUTH_BY_EMAIL_BUTTON)

    def enter_email(self, email):
        self.type(self.EMAIL_FIELD, email)

    def enter_auth_code(self, auth_code):
        self.type(self.AUTH_CODE_FIELD, auth_code)

    def click_submit_button(self):
        self.click_button(self.SUBMIT_BUTTON)

    def login_by_email(self, user):
        self.enter_email(user.email)
        self.click_submit_button()
        self.enter_auth_code(AUTH_CODE)
        self.click_submit_button()

    def torso_button_is_present(self):
        return self.is_present(self.TORSO_BUTTON)
    
    def authorization_modal_is_present(self):
        return self.is_present(self.AUTHORIZATION_MODAL)