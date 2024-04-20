import time
from locators import Stellarburgers
from data import StellarburgersServiceTestData
from faker import Faker

fake = Faker()

class TestRegistration:
    def test_successful_registration(self, driver):
        login_button = driver.find_element(*Stellarburgers.LOGIN_BUTTON_MAIN)
        login_button.click()

        registration_button = driver.find_element(*Stellarburgers.REGISTRATION_BUTTON)
        registration_button.click()

        username_input = driver.find_element(*Stellarburgers.USERNAME_INPUT)
        username_input.send_keys(StellarburgersServiceTestData.AUTH_NAME)

        email_input = driver.find_element(*Stellarburgers.EMAIL_INPUT)
        email_input.send_keys(fake.email())

        password_input = driver.find_element(*Stellarburgers.PASSWORD_INPUT)
        password_input.send_keys(StellarburgersServiceTestData.AUTH_PASSWORD)

        registration_button_main = driver.find_element(*Stellarburgers.REGISTRATION_BUTTON_MAIN)
        registration_button_main.click()
        time.sleep(2)
        login_name = driver.find_element(*Stellarburgers.LOGIN_NAME)
        assert login_name.is_displayed(), "Successful registration"

        driver.quit()