import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Contacts_page(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    button_ask = "[class*='omni-email-widget']" # локатор кнопки Задать вопрос

    # Getters

    def get_button_ask(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_ask)))

    # Actions

    def click_button_ask(self):
        self.get_button_ask().click()
        print("Click button ask")

    # Methods

    def select_contact_the_company(self):
        with allure.step("select_contact_the_company"):
            Logger.add_start_step(method="select_contact_the_company")
            self.get_current_url() # вызов нашего url
            self.scroll() # вызов метода scroll из Base
            time.sleep(3)
            self.get_screenshot() # вызов метода получения скриншота из Base
            self.click_button_ask() # метод нажатия кнопки Задать вопрос
            time.sleep(3)
            self.get_screenshot()  # вызов метода получения скриншота из Base
            Logger.add_end_step(url=self.driver.current_url, method="select_contact_the_company")
