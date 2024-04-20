from locators import Stellarburgers
from data import StellarburgersServiceTestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestLoginButtonRegistrationForm:
    def test_login_button_registration_form(self, driver):
        login_button = driver.find_element(*Stellarburgers.LOGIN_BUTTON_MAIN)
        login_button.click()

        registration_button = driver.find_element(*Stellarburgers.REGISTRATION_BUTTON)
        registration_button.click()


        login_button_from_registration = driver.find_element(*Stellarburgers.LOGIN_BUTTON_FROM_REGISTRATION)
        login_button_from_registration.click()

        email_input = driver.find_element(*Stellarburgers.EMAIL_INPUT)
        email_input.send_keys(StellarburgersServiceTestData.AUTH_EMAIL)

        password_input = driver.find_element(*Stellarburgers.PASSWORD_INPUT)
        password_input.send_keys(StellarburgersServiceTestData.AUTH_PASSWORD)

        login_button = driver.find_element(*Stellarburgers.LOGIN_BUTTON)
        login_button.click()

        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Stellarburgers.CHECKOUT_BUTTON)))
        assert element.is_displayed(), "Successful registration"
