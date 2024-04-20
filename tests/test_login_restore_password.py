import time
from locators import Stellarburgers
from data import StellarburgersServiceTestData

class TestLoginRestorePassword:
    def test_login_restore_password(self, driver):
        login_button = driver.find_element(*Stellarburgers.LOGIN_BUTTON_MAIN)
        login_button.click()

        restore_password_button = driver.find_element(*Stellarburgers.LOGIN_BUTTON_RESTORE_PASSWORD)
        restore_password_button.click()

        login_button_from_registration = driver.find_element(*Stellarburgers.LOGIN_BUTTON_FROM_REGISTRATION)
        login_button_from_registration.click()

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