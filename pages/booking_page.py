import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Booking_page(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    main_word = "[class='product-first-screen__name']" # локатор текста "TL: Booking Engine"
    why_booking_module = ".strip.strip_type-correct :nth-child(3) > a.tl-faq-accordion-title" # локатор меню "Зачем отелю модуль бронирования?"

    # Getters

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.main_word)))

    def get_why_booking_module(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.why_booking_module)))

    # Actions

    def click_why_booking_module(self):
        self.get_why_booking_module().click()
        print("Click why booking module")

    # Methods

    def select_booking_engine(self):
        with allure.step("select_booking_engine"):
            Logger.add_start_step(method="select_booking_engine")
            self.get_current_url() # вызов нашего url
            self.assert_word(self.get_main_word(), 'TL: BOOKING ENGINE')  # вызов метода сравнения текста на странице "TL: Booking Engine"
            self.scroll() # вызов метода scroll из Base
            time.sleep(3)
            self.get_screenshot() # вызов метода получения скриншота из Base
            self.click_why_booking_module() # метод нажатия кнопки (выбора меню) "Зачем отелю модуль бронирования?"
            Logger.add_end_step(url=self.driver.current_url, method="select_booking_engine")
