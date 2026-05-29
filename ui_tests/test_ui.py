from pages.landing_main_page import LandingMainPage
from pages.landing_profile_page import LandingProfilePage


def test_login(driver, test_user):
    landing_main_page = LandingMainPage(driver)

    landing_profile_page = LandingProfilePage(driver)

    landing_main_page.open_page()

    landing_main_page.torso_button_is_present()

    landing_main_page.open_authorization_modal()

    landing_main_page.authorization_modal_is_present()

    landing_main_page.select_auth_by_email()

    landing_main_page.login_by_email(test_user)

    assert landing_profile_page.page_is_loaded()
