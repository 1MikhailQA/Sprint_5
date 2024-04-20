import time
from locators import Stellarburgers
from data import StellarburgersServiceTestData



class TestLoginPersonalAccount:
    def test_login_personal_account(self, driver):
        personal_account_button_main = driver.find_element(*Stellarburgers.PERSONAL_ACCOUNT_BUTTON_MAIN)
        personal_account_button_main.click()

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