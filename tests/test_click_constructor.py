from locators import Stellarburgers
from data import StellarburgersServiceTestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestClickConstructor:
    def test_click_constructor(self, driver):
        login_button_main = driver.find_element(*Stellarburgers.LOGIN_BUTTON_MAIN)
        login_button_main.click()

        email_input = driver.find_element(*Stellarburgers.EMAIL_INPUT)
        email_input.send_keys(StellarburgersServiceTestData.AUTH_EMAIL)

        password_input = driver.find_element(*Stellarburgers.PASSWORD_INPUT)
        password_input.send_keys(StellarburgersServiceTestData.AUTH_PASSWORD)

        login_button = driver.find_element(*Stellarburgers.LOGIN_BUTTON)
        login_button.click()

        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Stellarburgers.CHECKOUT_BUTTON)))
        assert element.is_displayed(), "Successful registration"

        personal_account_button_main = driver.find_element(*Stellarburgers.PERSONAL_ACCOUNT_BUTTON_MAIN)
        personal_account_button_main.click()

        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Stellarburgers.PROFILE_HEADER)))
        assert element.is_displayed(), "In your personal account"

        button_constructor = driver.find_element(*Stellarburgers.BUTTON_CONSTRUCTOR_MAIN)
        button_constructor.click()

        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((Stellarburgers.CHECKOUT_BUTTON)))
        assert element.is_displayed(), "Successful registration"
