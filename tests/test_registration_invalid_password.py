from locators import Stellarburgers
from data import StellarburgersServiceTestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker


fake = Faker()
class TestRegistrationInvalidPassword:
    def test_registration_invalid_password(self, driver):

        login_button = driver.find_element(*Stellarburgers.LOGIN_BUTTON_MAIN)
        login_button.click()

        registration_button = driver.find_element(*Stellarburgers.REGISTRATION_BUTTON)
        registration_button.click()

        username_input = driver.find_element(*Stellarburgers.USERNAME_INPUT)
        username_input.send_keys(StellarburgersServiceTestData.AUTH_NAME)

        email_input = driver.find_element(*Stellarburgers.EMAIL_INPUT)
        email_input.send_keys(fake.email())

        password_input = driver.find_element(*Stellarburgers.PASSWORD_INPUT)
        password_input.send_keys(StellarburgersServiceTestData.AUTH_INVALID_PASSWORD)

        registration_button_main = driver.find_element(*Stellarburgers.REGISTRATION_BUTTON_MAIN)
        registration_button_main.click()

        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Stellarburgers.INVALID_PASSWORD)))
        assert element.is_displayed(), "Successful registration"

