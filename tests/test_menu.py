import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Stellarburgers
from data import StellarburgersServiceTestData

class TestMenu:
    def test_menu(self, driver):
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

        bread_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Stellarburgers.BREAD_BUTTON))
        driver.execute_script("arguments[0].scrollIntoView();", bread_button)
        driver.execute_script("arguments[0].click();", bread_button)
        time.sleep(2)
        bread_tab_element = driver.find_element(*Stellarburgers.CLASS_TAB)
        assert "tab_tab_type_current__2BEPc" in bread_tab_element.get_attribute("class")

        sauces_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Stellarburgers.SAUCES_BUTTON))
        driver.execute_script("arguments[0].scrollIntoView();", sauces_button)
        driver.execute_script("arguments[0].click();", sauces_button)
        time.sleep(2)
        sauces_tab_element = driver.find_element(*Stellarburgers.CLASS_TAB)
        assert "tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect" in sauces_tab_element.get_attribute("class")

        stuffings_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Stellarburgers.STUFFINGS_BUTTON))
        driver.execute_script("arguments[0].scrollIntoView();", stuffings_button)
        driver.execute_script("arguments[0].click();", stuffings_button)
        time.sleep(2)
        stuffings_tab_element = driver.find_element(*Stellarburgers.CLASS_TAB)
        assert "tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect" in stuffings_tab_element.get_attribute("class")

        driver.quit()
