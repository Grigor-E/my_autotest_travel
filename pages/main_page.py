import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class Main_page(Base):

    url = 'https://www.travelline.ru/'  # адрес главной страницы сайта Travelline

    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    menu_tools = ".clearfix :nth-child(1) > .desktop" # локатор меню "Инструменты"
    booking_module = ".clearfix :nth-child(1) > .ico-be" # локатор подменю "Модуль бронирования"
    control_system = ".clearfix :nth-child(2) > .ico-webpms" # локатор подменю "Система управления"
    channel_manager = ".clearfix :nth-child(3) > .ico-chm" # локатор подменю "Менеджер каналов"
    accepting_online_payments = ".clearfix :nth-child(1) > .menu-styled__item-subtitle"  # локатор подменю "Прием онлайн-платежей"
    work_with_reviews = ".clearfix :nth-child(2) > .menu-styled__item-subtitle"  # локатор подменю "Работа с отзывами"
    competitor_price_analysis = ".clearfix :nth-child(3) > .menu-styled__item-subtitle" # локатор подменю "Анализ цен конкурентов"
    integration_with_crm = ".clearfix :nth-child(4) > .menu-styled__item-subtitle" # локатор подменю "Интеграция с CRM"
    metasearch_engines = ".clearfix :nth-child(5) > .menu-styled__item-subtitle"  # локатор подменю "Метапоисковики"
    site_development = ".clearfix :nth-child(6) > .menu-styled__item-subtitle"  # локатор подменю "Разработка сайта"
    menu_prices = "[class*='desktop promo_price']" # локатор меню "Цены"
    menu_content = "[class*='desktop menu_blog']"  # локатор меню "Контент"
    menu_support = ".clearfix :nth-child(4) > .desktop"  # локатор меню "Поддержка"
    knowledge_base = ".clearfix :nth-child(4) > .clearfix :nth-child(1) > .clearfix" # локатор подменю "База знаний"
    booking_dashboard = ".clearfix :nth-child(4) > .clearfix :nth-child(2) > .clearfix"  # локатор подменю "Дашборд броней"
    menu_about_company = ".clearfix :nth-child(5) > .desktop"  # локатор меню "О компании"
    about_travelline = ".clearfix :nth-child(5) > .clearfix :nth-child(1) > .clearfix"  # локатор подменю "О TravelLine"
    reviews = ".clearfix :nth-child(5) > .clearfix :nth-child(2) > .clearfix"  # локатор подменю "Отзывы"
    events = ".clearfix :nth-child(3) > .clearfix"  # локатор подменю "Мероприятия"
    partners = ".clearfix :nth-child(4) > .menu-block__item-link"  # локатор подменю "Партнеры"
    career = ".clearfix :nth-child(5) > .menu-block__item-link"  # локатор подменю "Работа и стажировка"
    contacts = ".clearfix :nth-child(6) > .clearfix"  # локатор подменю "Контакты"

    # Getters

    def get_menu_tools(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.menu_tools)))

    def get_booking_module(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.booking_module)))

    def get_control_system(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.control_system)))

    def get_channel_manager(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.channel_manager)))

    def get_accepting_online_payments(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.accepting_online_payments)))

    def get_work_with_reviews(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.work_with_reviews)))

    def get_competitor_price_analysis(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.competitor_price_analysis)))

    def get_integration_with_crm(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.integration_with_crm)))

    def get_metasearch_engines(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.metasearch_engines)))

    def get_site_development(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.site_development)))
    
    def get_menu_prices(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.menu_prices)))

    def get_menu_content(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.menu_content)))

    def get_menu_support(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.menu_support)))

    def get_knowledge_base(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.knowledge_base)))

    def get_booking_dashboard(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.booking_dashboard)))

    def get_menu_about_company(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.menu_about_company)))

    def get_about_travelline(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.about_travelline)))

    def get_reviews(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.reviews)))

    def get_events(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.events)))

    def get_partners(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.partners)))

    def get_career(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.career)))

    def get_contacts(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.contacts)))

    # Actions

    def click_menu_tools(self):
        self.get_menu_tools().click()
        print("Click menu tools")

    def click_booking_module(self):
        self.get_booking_module().click()
        print("Click booking module")

    def click_control_system(self):
        self.get_control_system().click()
        print("Click control system")

    def click_channel_manager(self):
        self.get_channel_manager().click()
        print("Click channel manager")

    def click_accepting_online_payments(self):
        self.get_accepting_online_payments().click()
        print("Click accepting online payments")

    def click_work_with_reviews(self):
        self.get_work_with_reviews().click()
        print("Click work with reviews")

    def click_competitor_price_analysis(self):
        self.get_competitor_price_analysis().click()
        print("Click competitor price analysis")

    def click_integration_with_crm(self):
        self.get_integration_with_crm().click()
        print("Click integration with crm")

    def click_metasearch_engines(self):
        self.get_metasearch_engines().click()
        print("Click metasearch engines")

    def click_site_development(self):
        self.get_site_development().click()
        print("Click site development")
        
    def click_menu_prices(self):
        self.get_menu_prices().click()
        print("Click menu prices")

    def click_menu_content(self):
        self.get_menu_content().click()
        print("Click menu content")

    def click_menu_support(self):
        self.get_menu_support().click()
        print("Click menu support")

    def click_knowledge_base(self):
        self.get_knowledge_base().click()
        print("Click knowledge base")

    def click_booking_dashboard(self):
        self.get_booking_dashboard().click()
        print("Click booking dashboard")

    def click_menu_about_company(self):
        self.get_menu_about_company().click()
        print("Click menu about company")

    def click_about_travelline(self):
        self.get_about_travelline().click()
        print("Click about TravelLine")

    def click_reviews(self):
        self.get_reviews().click()
        print("Click reviews")

    def click_events(self):
        self.get_events().click()
        print("Click events")

    def click_partners(self):
        self.get_partners().click()
        print("Click partners")

    def click_career(self):
        self.get_career().click()
        print("Click career")

    def click_contacts(self):
        self.get_contacts().click()
        print("Click contacts")

    # Methods

    def select_booking_module(self):
        with allure.step("select_booking_module"):
            Logger.add_start_step(method="select_booking_module")
            self.driver.get(self.url)  # метод октрытия страницы
            self.driver.maximize_window()  # метод открытия во весь экран
            self.get_current_url() # вызов нашего url
            self.click_menu_tools() # метод нажатия кнопки выбора меню "Инструменты"
            self.click_booking_module() # метод нажатия на подменю "Модуль бронирования"
            self.assert_url('https://www.travelline.ru/products/tl-hotel/') # метод сравнения URL
            Logger.add_end_step(url=self.driver.current_url, method="select_booking_module")

    def select_control_system(self):
        with allure.step("select_control_system"):
            Logger.add_start_step(method="select_control_system")
            self.driver.get(self.url)  # метод октрытия страницы
            self.driver.maximize_window()  # метод открытия во весь экран
            self.get_current_url() # вызов нашего url
            self.click_menu_tools() # метод нажатия кнопки выбора меню "Инструменты"
            self.click_control_system() # метод нажатия на подменю "Система управления"
            self.assert_url('https://www.travelline.ru/products/webpms/') # метод сравнения URL
            Logger.add_end_step(url=self.driver.current_url, method="select_control_system")

    def select_channel_manager(self):
        with allure.step("select_channel_manager"):
            Logger.add_start_step(method="select_channel_manager")
            self.driver.get(self.url)  # метод октрытия страницы
            self.driver.maximize_window()  # метод открытия во весь экран
            self.get_current_url() # вызов нашего url
            self.click_menu_tools() # метод нажатия кнопки выбора меню "Инструменты"
            self.click_channel_manager() # метод нажатия на подменю "Менеджер каналов"
            self.assert_url('https://www.travelline.ru/products/channel-manager/') # метод сравнения URL
            Logger.add_end_step(url=self.driver.current_url, method="select_channel_manager")

    def select_accepting_online_payments(self):
        with allure.step("select_accepting_online_payments"):
            Logger.add_start_step(method="select_accepting_online_payments")
            self.driver.get(self.url)  # метод октрытия страницы
            self.driver.maximize_window()  # метод открытия во весь экран
            self.get_current_url() # вызов нашего url
            self.click_menu_tools() # метод нажатия кнопки выбора меню "Инструменты"
            self.click_accepting_online_payments() # метод нажатия на подменю "Прием онлайн-платежей"
            self.assert_url('https://www.travelline.ru/products/order-management/') # метод сравнения URL
            Logger.add_end_step(url=self.driver.current_url, method="select_accepting_online_payments")

    def select_work_with_reviews(self):
        with allure.step("select_work_with_reviews"):
            Logger.add_start_step(method="select_work_with_reviews")
            self.driver.get(self.url)  # метод октрытия страницы
            self.driver.maximize_window()  # метод открытия во весь экран
            self.get_current_url() # вызов нашего url
            self.click_menu_tools() # метод нажатия кнопки выбора меню "Инструменты"
            self.click_work_with_reviews() # метод нажатия на подменю "Работа с отзывами"
            self.assert_url('https://www.travelline.ru/products/reputation/') # метод сравнения URL
            Logger.add_end_step(url=self.driver.current_url, method="select_work_with_reviews")

    def select_competitor_price_analysis(self):
        with allure.step("select_competitor_price_analysis"):
            Logger.add_start_step(method="select_competitor_price_analysis")
            self.driver.get(self.url)  # метод октрытия страницы
            self.driver.maximize_window()  # метод открытия во весь экран
            self.get_current_url() # вызов нашего url
            self.click_menu_tools() # метод нажатия кнопки выбора меню "Инструменты"
            self.click_competitor_price_analysis() # метод нажатия на подменю "Анализ цен конкурентов"
            self.assert_url('https://www.travelline.ru/products/rate-shopper/') # метод сравнения URL
            Logger.add_end_step(url=self.driver.current_url, method="select_competitor_price_analysis")

    def select_integration_with_crm(self):
        with allure.step("select_integration_with_crm"):
            Logger.add_start_step(method="select_integration_with_crm")
            self.driver.get(self.url)  # метод октрытия страницы
            self.driver.maximize_window()  # метод открытия во весь экран
            self.get_current_url() # вызов нашего url
            self.click_menu_tools() # метод нажатия кнопки выбора меню "Инструменты"
            self.click_integration_with_crm() # метод нажатия на подменю "Интеграция с CRM"
            self.assert_url('https://www.travelline.ru/products/crm/') # метод сравнения URL
            Logger.add_end_step(url=self.driver.current_url, method="select_integration_with_crm")

    def select_metasearch_engines(self):
        with allure.step("select_metasearch_engines"):
            Logger.add_start_step(method="select_metasearch_engines")
            self.driver.get(self.url)  # метод октрытия страницы
            self.driver.maximize_window()  # метод открытия во весь экран
            self.get_current_url() # вызов нашего url
            self.click_menu_tools() # метод нажатия кнопки выбора меню "Инструменты"
            self.click_metasearch_engines() # метод нажатия на подменю "Метапоисковики"
            self.assert_url('https://www.travelline.ru/products/metasearch/') # метод сравнения URL
            Logger.add_end_step(url=self.driver.current_url, method="select_metasearch_engines")

    def select_site_development(self):
        with allure.step("select_site_development"):
            Logger.add_start_step(method="select_site_development")
            self.driver.get(self.url)  # метод октрытия страницы
            self.driver.maximize_window()  # метод открытия во весь экран
            self.get_current_url() # вызов нашего url
            self.click_menu_tools() # метод нажатия кнопки выбора меню "Инструменты"
            self.click_site_development() # метод нажатия на подменю "Разработка сайта"
            self.assert_url('https://www.travelline.ru/products/tl-site/') # метод сравнения URL
            Logger.add_end_step(url=self.driver.current_url, method="select_site_development")

    def select_menu_prices(self):
        with allure.step("select_menu_prices"):
            Logger.add_start_step(method="select_menu_prices")
            self.driver.get(self.url)  # метод октрытия страницы
            self.driver.maximize_window()  # метод открытия во весь экран
            self.get_current_url() # вызов нашего url
            self.click_menu_prices() # метод нажатия на меню "Цены"
            self.assert_url('https://www.travelline.ru/price/') # метод сравнения URL
            Logger.add_end_step(url=self.driver.current_url, method="select_menu_prices")

    def select_menu_content(self):
        with allure.step("select_menu_content"):
            Logger.add_start_step(method="select_menu_content")
            self.driver.get(self.url)  # метод октрытия страницы
            self.driver.maximize_window()  # метод открытия во весь экран
            self.get_current_url() # вызов нашего url
            self.click_menu_content() # метод нажатия на меню "Контент"
            self.assert_url('https://www.travelline.ru/blog/') # метод сравнения URL
            Logger.add_end_step(url=self.driver.current_url, method="select_menu_content")

    def select_knowledge_base(self):
        with allure.step("select_knowledge_base"):
            Logger.add_start_step(method="select_knowledge_base")
            self.driver.get(self.url)  # метод октрытия страницы
            self.driver.maximize_window()  # метод открытия во весь экран
            self.get_current_url()  # вызов нашего url
            self.click_menu_support()  # метод нажатия кнопки выбора меню "Поддержка"
            self.click_knowledge_base()  # метод нажатия на подменю "База знаний"
            self.assert_url('https://www.travelline.ru/support/knowledge-base/')  # метод сравнения URL
            Logger.add_end_step(url=self.driver.current_url, method="select_knowledge_base")

    def select_booking_dashboard(self):
        with allure.step("select_booking_dashboard"):
            Logger.add_start_step(method="select_booking_dashboard")
            self.driver.get(self.url)  # метод октрытия страницы
            self.driver.maximize_window()  # метод открытия во весь экран
            self.get_current_url()  # вызов нашего url
            self.click_menu_support()  # метод нажатия кнопки выбора меню "Поддержка"
            self.click_booking_dashboard()  # метод нажатия на подменю "Дашборд броней"
            self.assert_url('https://www.travelline.ru/blog/dashboard/')  # метод сравнения URL
            Logger.add_end_step(url=self.driver.current_url, method="select_booking_dashboard")

    def select_about_travelline(self):
        with allure.step("select_about_travelline"):
            Logger.add_start_step(method="select_about_travelline")
            self.driver.get(self.url)  # метод октрытия страницы
            self.driver.maximize_window()  # метод открытия во весь экран
            self.get_current_url()  # вызов нашего url
            self.click_menu_about_company()  # метод нажатия кнопки выбора меню "О компании"
            self.click_about_travelline()  # метод нажатия на подменю "О TravelLine"
            self.assert_url('https://www.travelline.ru/about/')  # метод сравнения URL
            Logger.add_end_step(url=self.driver.current_url, method="select_about_travelline")

    def select_reviews(self):
        with allure.step("select_reviews"):
            Logger.add_start_step(method="select_reviews")
            self.driver.get(self.url)  # метод октрытия страницы
            self.driver.maximize_window()  # метод открытия во весь экран
            self.get_current_url()  # вызов нашего url
            self.click_menu_about_company()  # метод нажатия кнопки выбора меню "О компании"
            self.click_reviews()  # метод нажатия на подменю "Отзывы"
            self.assert_url('https://www.travelline.ru/about/reviews/')  # метод сравнения URL
            Logger.add_end_step(url=self.driver.current_url, method="select_reviews")

    def select_events(self):
        with allure.step("select_events"):
            Logger.add_start_step(method="select_events")
            self.driver.get(self.url)  # метод октрытия страницы
            self.driver.maximize_window()  # метод открытия во весь экран
            self.get_current_url()  # вызов нашего url
            self.click_menu_about_company()  # метод нажатия кнопки выбора меню "О компании"
            self.click_events()  # метод нажатия на подменю "Мероприятия"
            self.assert_url('https://www.travelline.ru/about/events/')  # метод сравнения URL
            Logger.add_end_step(url=self.driver.current_url, method="select_events")

    def select_partners(self):
        with allure.step("select_partners"):
            Logger.add_start_step(method="select_partners")
            self.driver.get(self.url)  # метод октрытия страницы
            self.driver.maximize_window()  # метод открытия во весь экран
            self.get_current_url()  # вызов нашего url
            self.click_menu_about_company()  # метод нажатия кнопки выбора меню "О компании"
            self.click_partners()  # метод нажатия на подменю "Партнеры"
            self.assert_url('https://www.travelline.ru/about/technical-partners/ids-ota/')  # метод сравнения URL
            Logger.add_end_step(url=self.driver.current_url, method="select_partners")

    def select_career(self):
        with allure.step("select_career"):
            Logger.add_start_step(method="select_career")
            self.driver.get(self.url)  # метод октрытия страницы
            self.driver.maximize_window()  # метод открытия во весь экран
            self.get_current_url()  # вызов нашего url
            self.click_menu_about_company()  # метод нажатия кнопки выбора меню "О компании"
            self.click_career()  # метод нажатия на подменю "Работа и стажировка"
            self.assert_url('https://www.travelline.ru/career/')  # метод сравнения URL
            Logger.add_end_step(url=self.driver.current_url, method="select_career")

    def select_contacts(self):
        with allure.step("select_contacts"):
            Logger.add_start_step(method="select_contacts")
            self.driver.get(self.url)  # метод октрытия страницы
            self.driver.maximize_window()  # метод открытия во весь экран
            self.get_current_url()  # вызов нашего url
            self.click_menu_about_company()  # метод нажатия кнопки выбора меню "О компании"
            self.click_contacts()  # метод нажатия на подменю "Контакты"
            self.assert_url('https://www.travelline.ru/contacts/')  # метод сравнения URL
            Logger.add_end_step(url=self.driver.current_url, method="select_contacts")