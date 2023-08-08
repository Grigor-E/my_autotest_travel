import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

# ДЛЯ ПРОХОЖДЕНИЯ ШАГА АВТОРИЗАЦИИ НЕОБХОДИМО ВВЕСТИ ЛОГИН И ПАРОЛЬ В КАЧЕСТВЕ КЛЮЧЕЙ ДЛЯ ОТПРАВКИ.

class Login_page(Base):

    url = 'https://secure.travelline.ru/secure/Enter.aspx?ReturnUrl=%2fsecure%2f' # адрес страницы авторизации на сайте Travelline

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    user_name = "[name='username']" # локатор поля ввода логина
    password = "[name='password']" # локатор поля ввода пароля
    login_button = "[class='btn btn-md btn-primary']" # локатор кнопки Войти
    main_word = "8 800 555-20-30" # локатор текста на странице после перехода (переход после авторизации)
    error_message = "[class='ng-binding']" # локатор сообщения об ошибке

    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.main_word)))

    def get_error_message(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.error_message)))

    # Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    # Methods

    def authorization(self):
        with allure.step("authorization"):
            Logger.add_start_step(method="authorization")
            self.driver.get(self.url) # метод октрытия страницы
            self.driver.maximize_window() # метод открытия во весь экран
            self.get_current_url() # вызов нашего url
            self.input_user_name("ВВЕСТИ КОРРЕКТНЫЙ ЛОГИН") # метод заполнения поля логина
            self.input_password("ВВЕСТИ КОРРЕКТНЫЙ ПАРОЛЬ") # метод заполнения поля пароля
            self.click_login_button() # метод нажатия кнопки Вход
            # self.assert_word(self.get_main_word(), '8 800 555-20-30') # вызов метода сравнения текста на странице после перехода
            Logger.add_end_step(url=self.driver.current_url, method="authorization")

    def not_authorization(self):
        with allure.step("not_authorization"):
            Logger.add_start_step(method="not_authorization")
            self.driver.get(self.url) # метод октрытия страницы
            self.driver.maximize_window() # метод открытия во весь экран
            self.get_current_url() # вызов нашего url

            # ВВЕСТИ НЕКОРРЕКТНЫЕ ДАННЫЕ ЛОГИНА И/ИЛИ ПАРОЛЯ (оставить поле логина и/или поле пароля пустым(и))

            self.input_user_name("ВВЕСТИ ЛОГИН") # метод заполнения поля логина
            self.input_password("ВВЕСТИ ПАРОЛЬ") # метод заполнения поля пароля
            self.click_login_button() # метод нажатия кнопки Вход
            self.assert_word(self.get_error_message(), 'Неверный логин или пароль.') # вызов метода сравнения сообщения об ошибке
            Logger.add_end_step(url=self.driver.current_url, method="not_authorization")

