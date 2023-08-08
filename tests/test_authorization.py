import pytest
import allure
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import Login_page


@allure.description("test good authorization")
@pytest.mark.run(order=1)
def test_good_authorization(set_group, set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(options=options)

    print("Start test good authorization")

    lp = Login_page(driver)
    lp.authorization()

    print("Finish test good authorization")
    driver.quit()

@allure.description("test not authorization")
@pytest.mark.run(order=2)
def test_not_authorization(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.WebDriver(options=options)

    print("Start test not authorization")

    lp = Login_page(driver)
    lp.not_authorization()

    print("Появилось сообщение об ошибке")

    print("Finish test not authorization")
    driver.quit()