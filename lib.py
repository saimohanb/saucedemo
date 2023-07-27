from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_cond


class Helper:
    def __init__(self, web_driver):
        self.driver = web_driver
        self.max_timeout = 180
        self.lag = 3

    def scroll_into_view(self, web_driver, web_object):
        web_driver.execute_script("arguments[0].scrollIntoView(false);", web_driver.find_element(web_object[0], web_object[1]))

    def wait_for_visible(self, web_driver, web_object, timeout_override=None):
        locator = (web_object[0], web_object[1])
        if timeout_override:
            wait = WebDriverWait(web_driver, timeout_override*self.lag)
        else:
            wait = WebDriverWait(web_driver, self.max_timeout)
        wait.until(exp_cond.visibility_of_element_located(locator))

    def web_object_is_visible(self, web_driver, web_object, timeout_override=None):
        visible = False
        try:
            self.wait_for_visible(web_object=web_object, timeout_override=timeout_override, web_driver=web_driver)
            self.scroll_into_view(web_object=web_object, web_driver=web_driver)
            visible = True
            return True
        except Exception:
            return False
        finally:
            if visible:
                print(f"Web object is visible {web_object}")
