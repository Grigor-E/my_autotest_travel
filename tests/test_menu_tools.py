import pytest
import allure
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from pages.contacts_page import Contacts_page
from pages.main_page import Main_page


@allure.description("test booking module")
@pytest.mark.run(order=3)
def test_booking_module(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(chrome_options=options)

    print("Start test booking module")

    mp = Main_page(driver)
    mp.select_booking_module()

    print("Finish test booking module")
    driver.quit()

@allure.description("test control system")
@pytest.mark.run(order=4)
def test_control_system(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(chrome_options=options)

    print("Start test control system")

    mp = Main_page(driver)
    mp.select_control_system()

    print("Finish test control system")
    driver.quit()

@allure.description("test channel manager")
@pytest.mark.run(order=5)
def test_channel_manager(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(chrome_options=options)

    print("Start test channel manager")

    mp = Main_page(driver)
    mp.select_channel_manager()

    print("Finish test channel manager")
    driver.quit()

@allure.description("test accepting online payments")
@pytest.mark.run(order=6)
def test_accepting_online_payments(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(chrome_options=options)

    print("Start test accepting online payments")

    mp = Main_page(driver)
    mp.select_accepting_online_payments()

    print("Finish test accepting online payments")
    driver.quit()

@allure.description("test work with reviews")
@pytest.mark.run(order=7)
def test_work_with_reviews(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(chrome_options=options)

    print("Start test work with reviews")

    mp = Main_page(driver)
    mp.select_work_with_reviews()

    print("Finish test work with reviews")
    driver.quit()

@allure.description("test competitor price analysis")
@pytest.mark.run(order=8)
def test_competitor_price_analysis(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(chrome_options=options)

    print("Start test competitor price analysis")

    mp = Main_page(driver)
    mp.select_competitor_price_analysis()

    print("Finish test competitor price analysis")
    driver.quit()

@allure.description("test integration with crm")
@pytest.mark.run(order=9)
def test_integration_with_crm(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(chrome_options=options)

    print("Start test integration with crm")

    mp = Main_page(driver)
    mp.select_integration_with_crm()

    print("Finish test integration with crm")
    driver.quit()

@allure.description("test metasearch engines")
@pytest.mark.run(order=10)
def test_metasearch_engines(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(chrome_options=options)

    print("Start test metasearch engines")

    mp = Main_page(driver)
    mp.select_metasearch_engines()

    print("Finish test metasearch engines")
    driver.quit()

@allure.description("test site development")
@pytest.mark.run(order=11)
def test_site_development(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(chrome_options=options)

    print("Start test site development")

    mp = Main_page(driver)
    mp.select_site_development()

    print("Finish test site development")
    driver.quit()

@allure.description("test menu prices")
@pytest.mark.run(order=12)
def test_menu_prices(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(chrome_options=options)

    print("Start test menu prices")

    mp = Main_page(driver)
    mp.select_menu_prices()

    print("Finish test menu prices")
    driver.quit()

@allure.description("test menu content")
@pytest.mark.run(order=13)
def test_menu_content(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(chrome_options=options)

    print("Start test menu content")

    mp = Main_page(driver)
    mp.select_menu_content()

    print("Finish test menu content")
    driver.quit()

@allure.description("test knowledge base")
@pytest.mark.run(order=14)
def test_knowledge_base(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(chrome_options=options)

    print("Start test knowledge base")

    mp = Main_page(driver)
    mp.select_knowledge_base()

    print("Finish test knowledge base")
    driver.quit()

@allure.description("test booking dashboard")
@pytest.mark.run(order=15)
def test_booking_dashboard(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(chrome_options=options)

    print("Start test booking dashboard")

    mp = Main_page(driver)
    mp.select_booking_dashboard()

    print("Finish test booking dashboard")
    driver.quit()

@allure.description("test about travelline")
@pytest.mark.run(order=16)
def test_about_travelline(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(chrome_options=options)

    print("Start test about travelline")

    mp = Main_page(driver)
    mp.select_about_travelline()

    print("Finish test about travelline")
    driver.quit()

@allure.description("test reviews")
@pytest.mark.run(order=17)
def test_reviews(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(chrome_options=options)

    print("Start test reviews")

    mp = Main_page(driver)
    mp.select_reviews()

    print("Finish test reviews")
    driver.quit()

@allure.description("test events")
@pytest.mark.run(order=18)
def test_events(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(chrome_options=options)

    print("Start test events")

    mp = Main_page(driver)
    mp.select_events()

    print("Finish test events")
    driver.quit()

@allure.description("test partners")
@pytest.mark.run(order=19)
def test_partners(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(chrome_options=options)

    print("Start test partners")

    mp = Main_page(driver)
    mp.select_partners()

    print("Finish test partners")
    driver.quit()

@allure.description("test career")
@pytest.mark.run(order=20)
def test_career(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(chrome_options=options)

    print("Start test career")

    mp = Main_page(driver)
    mp.select_career()

    print("Finish test career")
    driver.quit()

@allure.description("test contacts")
@pytest.mark.run(order=21)
def test_contacts(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(chrome_options=options)

    print("Start test contacts")

    mp = Main_page(driver)
    mp.select_contacts()

    cp = Contacts_page(driver)
    cp.select_contact_the_company()

    print("Finish test contacts")
    driver.quit()