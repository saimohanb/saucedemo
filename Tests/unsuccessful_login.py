import allure

from selenium import webdriver
from Saucedemo.Pages.Login import LoginPage

driver = webdriver.Chrome()
url = 'https://www.saucedemo.com/'

data = {
    "username": "",
    "password": "secret_sauce"
}

login_page = LoginPage(driver=driver)


@allure.feature("Un-Authorized")
@allure.description("Unsuccessful Login")
def unsuccessful_login():
    driver.get(url)
    login_page.perform_complete_login(username=data['username'], password=data['password'])
    driver.quit()


unsuccessful_login()
