import time
from locators import Stellarburgers
from data import StellarburgersServiceTestData

class TestLoginToAccount:
    def test_login_to_account(self, driver):
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

        driver.quit()