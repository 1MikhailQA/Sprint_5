from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Stellarburgers
from data import StellarburgersServiceTestData

class TestMenuSaucesTab:
    def test_menu_sauces_tab(self, driver):
        login_button_main = driver.find_element(*Stellarburgers.LOGIN_BUTTON_MAIN)
        login_button_main.click()

        email_input = driver.find_element(*Stellarburgers.EMAIL_INPUT)
        email_input.send_keys(StellarburgersServiceTestData.AUTH_EMAIL)

        password_input = driver.find_element(*Stellarburgers.PASSWORD_INPUT)
        password_input.send_keys(StellarburgersServiceTestData.AUTH_PASSWORD)

        login_button = driver.find_element(*Stellarburgers.LOGIN_BUTTON)
        login_button.click()

        button_constructor = driver.find_element(*Stellarburgers.BUTTON_CONSTRUCTOR_MAIN)
        button_constructor.click()

        sauces_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Stellarburgers.SAUCES_BUTTON))
        driver.execute_script("arguments[0].scrollIntoView();", sauces_button)
        driver.execute_script("arguments[0].click();", sauces_button)

        sauces_tab_element = driver.find_element(*Stellarburgers.CLASS_TAB)
        assert "tab_tab__1SPyG" in sauces_tab_element.get_attribute("class")