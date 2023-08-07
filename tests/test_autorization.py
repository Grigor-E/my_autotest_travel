import pytest
import allure
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import Login_page


@allure.description("test good autorization")
@pytest.mark.run(order=1)
def test_good_autorization(set_group, set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(options=options)

    print("Start test good autorization")

    login = Login_page(driver)
    login.autorization()

    print("Finish test good autorization")
    driver.quit()

@allure.description("test not autorization")
@pytest.mark.run(order=2)
def test_not_autorization(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(options=options)

    print("Start test not autorization")

    login = Login_page(driver)
    login.not_autorization()

    print("Появилось сообщение об ошибке")

    print("Finish test not autorization")
    driver.quit()