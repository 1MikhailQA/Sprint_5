import time
from locators import Stellarburgers
from data import StellarburgersServiceTestData

class TestExitButtonClick:
    def test_exit_button_click(self, driver):
        login_button_main = driver.find_element(*Stellarburgers.LOGIN_BUTTON_MAIN)
        login_button_main.click()

        email_input = driver.find_element(*Stellarburgers.EMAIL_INPUT)
        email_input.send_keys(StellarburgersServiceTestData.AUTH_EMAIL)

        password_input = driver.find_element(*Stellarburgers.PASSWORD_INPUT)
        password_input.send_keys(StellarburgersServiceTestData.AUTH_PASSWORD)

        login_button = driver.find_element(*Stellarburgers.LOGIN_BUTTON)
        login_button.click()

        personal_account_button_main = driver.find_element(*Stellarburgers.PERSONAL_ACCOUNT_BUTTON_MAIN)
        personal_account_button_main.click()
        time.sleep(2)
        exit_button = driver.find_element(*Stellarburgers.EXIT_BUTTON)
        exit_button.click()

        time.sleep(2)
        login_name = driver.find_element(*Stellarburgers.LOGIN_NAME)
        assert login_name.is_displayed(), "Successful exit"

        driver.quit()