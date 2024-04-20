import time
from locators import Stellarburgers
from data import StellarburgersServiceTestData

class TestClickLogo:
    def test_click_logo(self, driver):
        login_button_main = driver.find_element(*Stellarburgers.LOGIN_BUTTON_MAIN)
        login_button_main.click()

        email_input = driver.find_element(*Stellarburgers.EMAIL_INPUT)
        email_input.send_keys(StellarburgersServiceTestData.AUTH_EMAIL)

        password_input = driver.find_element(*Stellarburgers.PASSWORD_INPUT)
        password_input.send_keys(StellarburgersServiceTestData.AUTH_PASSWORD)

        login_button = driver.find_element(*Stellarburgers.LOGIN_BUTTON)
        login_button.click()

        time.sleep(2)
        checkout_button = driver.find_element(*Stellarburgers.CHECKOUT_BUTTON)
        assert checkout_button.is_displayed(), "Successful login"

        personal_account_button_main = driver.find_element(*Stellarburgers.PERSONAL_ACCOUNT_BUTTON_MAIN)
        personal_account_button_main.click()

        time.sleep(2)
        profile_header = driver.find_element(*Stellarburgers.PROFILE_HEADER)
        assert profile_header.is_displayed(), "In your personal account"

        click_logo = driver.find_element(*Stellarburgers.BUTTON_LOGO_MAIN)
        click_logo.click()

        time.sleep(2)
        checkout_button = driver.find_element(*Stellarburgers.CHECKOUT_BUTTON)
        assert checkout_button.is_displayed(), "Home page"


        driver.quit()