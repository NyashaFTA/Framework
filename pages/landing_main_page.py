from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.environments import BASE_URL
from config.settings import AUTH_CODE

class LandingMainPage(BasePage):
    URL = BASE_URL

    TORSO_BUTTON = (By.CLASS_NAME, "auth-button")
    AUTHORIZATION_MODAL = (By.CLASS_NAME, "authorization__start")
    ENTER_CREDENTIALS_MODAL = (By.CLASS_NAME, "authorization__form")
    AUTH_BY_EMAIL_BUTTON = (By.CLASS_NAME, "authorization__email-button")
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[inputmode="email"]')
    AUTH_CODE_FIELD = (By.ID, "id-single-factor-code-text-field")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    CONSENT_MODAL = (By.XPATH, "//div[contains(@class, 'authorization')][.//div[contains(text(), 'Ваш аккаунт создан')]]")
    SKIP_CONSENT_MODAL_BUTTON = (By.CLASS_NAME, "authorization__skip-button")


    def open_page(self):
        self.go_to(self.URL)

    def open_authorization_modal(self):
        self.click_button(self.TORSO_BUTTON)

    def select_auth_by_email(self):
        self.click_button(self.AUTH_BY_EMAIL_BUTTON)

    def enter_email(self, email):
        self.type(self.EMAIL_FIELD, email)

    def enter_auth_code(self, auth_code):
        self.type_otp_code(self.AUTH_CODE_FIELD, auth_code)

    def click_submit_button(self):
        self.click_button(self.SUBMIT_BUTTON)

    def login_by_email(self, user):
        self.enter_email(user.email)
        self.click_submit_button()
        self.enter_auth_code(AUTH_CODE)

    def skip_consent_modal(self):
        self.click_button(self.SKIP_CONSENT_MODAL_BUTTON)

    def torso_button_is_visible(self):
        return self.is_visible(self.TORSO_BUTTON)
    
    def authorization_modal_is_visible(self):
        return self.is_visible(self.AUTHORIZATION_MODAL)
    
    def enter_credentials_modal_is_visible(self):
        return self.is_visible(self.ENTER_CREDENTIALS_MODAL)
    
    def consent_modal_is_visible(self):
        return self.is_visible(self.CONSENT_MODAL)

    def auth_code_field_is_visible(self):
        return self.is_visible(self.AUTH_CODE_FIELD)
    