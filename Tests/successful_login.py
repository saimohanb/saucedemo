import allure

from time import sleep
from selenium import webdriver
from saucedemo.Pages.Login import LoginPage

driver = webdriver.Chrome()
url = 'https://www.saucedemo.com/'

data = {
    "username": "standard_user",
    "password": "secret_sauce"
}

login_page = LoginPage(driver=driver)


@allure.feature("Authenticate")
@allure.description("Successful Login")
def successful_login():
    driver.get(url)
    login_page.perform_complete_login(username=data['username'], password=data['password'])
    driver.quit()
    sleep(5)


successful_login()
