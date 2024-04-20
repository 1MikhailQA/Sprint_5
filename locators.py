from selenium.webdriver.common.by import By

class Stellarburgers:
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text() = 'Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    REGISTRATION_BUTTON = (By.XPATH, "//a[text() = 'Зарегистрироваться']") # Кнопка "Зарегистрироваться"
    USERNAME_INPUT = (By.XPATH, "//input[@name='name']") #Поле имя
    EMAIL_INPUT = (By.XPATH, "//div[label[text()='Email']]/input[@name='name']") #Поле email
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and @name='Пароль']") #Поле passwodr
    REGISTRATION_BUTTON_MAIN = (By.XPATH, "//button[text() = 'Зарегистрироваться']") # Кнопка "Зарегистрироваться"

    LOGIN_NAME = (By.XPATH, "//h2[text() = 'Вход']") #Элемент на странице - "Вход"
    INVALID_PASSWORD = (By.XPATH, "//p[text() = 'Некорректный пароль']") #Сообщение о некорректном пароле

    LOGIN_BUTTON = (By.XPATH, "//button[text() = 'Войти']") # Кнопка "Войти"
    CHECKOUT_BUTTON = (By.XPATH, "//button[text() = 'Оформить заказ']")  #Кнопка "Оформить заказ"

    PERSONAL_ACCOUNT_BUTTON_MAIN = (By.XPATH, "//p[text() = 'Личный Кабинет']")  #Кнопка "Личный Кабинет"

    LOGIN_BUTTON_FROM_REGISTRATION = (By.XPATH, "//a[text() = 'Войти']") #Кнопка "Войти" в форме для регистрации

    LOGIN_BUTTON_RESTORE_PASSWORD = (By.XPATH, "//a[text() = 'Восстановить пароль']")  #Кнопка "Восстановить пароль"

    PROFILE_HEADER = (By.XPATH, "//a[text() = 'Профиль']") #Элемент на старнице - "Профиль"

    BUTTON_CONSTRUCTOR_MAIN = (By.XPATH, "//p[text() = 'Конструктор']")  # Кнопка "Конструктор"

    BUTTON_LOGO_MAIN = (By.XPATH, "//*[@id='root']/div/header/nav/div/a") #Логотип

    EXIT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")  # Кнопка "Выход"

    BREAD_BUTTON = (By.XPATH, "//span[text()='Булки']") # Кнопка "Булки"

    SAUCES_BUTTON = (By.XPATH, "//span[text()='Соусы']") # Кнопка "Соусы"

    STUFFINGS_BUTTON = (By.XPATH, "//span[text()='Начинки']") # Кнопка "Начинки"

    CLASS_TAB = (By.CLASS_NAME, "tab_tab__1SPyG")   #Класс для кнопок