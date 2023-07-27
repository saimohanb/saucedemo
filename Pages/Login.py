from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Support.lib import Helper


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def click_login(self):
        self.driver.find_element(By.CLASS_NAME, "btn_action").click()
        WebDriverWait(self.driver, 5).until(EC.url_changes)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def enter_username(self, username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def perform_complete_login(self, username, password):
        helper = Helper(web_driver=self.driver)
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        element = (By.XPATH, "//*[contains(@class,'error-message')]/h3")
        if helper.web_object_is_visible(web_driver=self.driver, web_object=element,
                                        timeout_override=5):
            text = self.driver.find_element(By.XPATH, "//*[contains(@class,'error-message')]/h3")
            print(f"error_text = {text.text}")
