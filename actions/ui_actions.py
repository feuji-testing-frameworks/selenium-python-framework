from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException, ElementNotInteractableException

class UI_Actions :

    """Intilize the webdriver"""
    def __init__(self,driver) :
        self.driver = driver;

    """This function is used for clicking the web element"""
    def webElement_click(self,locator) :
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).click();

    """This function is used for entering the text into the web element"""
    def webElement_input(self,locator,text) :
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(locator)).send_keys(text);

    """This function is used for entering the text into the web element"""
    def webElement_text(self,locator) :
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).text;

    """This function is used for scrolling the web element"""
    def scroll_to_element(self,locator) :
        self.driver.execute_script("window.scrollBy(0, arguments[0].offsetTop);", locator);
        WebDriverWait(self.driver,self.get_wait_time()).until(EC.visibility_of_element_located(locator));

    """This function is used for checking the web element is displayed or not"""
    def webElement_isDisplayed(self,locator) :
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).is_displayed();

    """This function is used for clearing the input fields"""
    def webElement_input_clear(self,locator) :
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).clear();

    def is_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def is_editable(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))
            return element.is_enabled()
        except (TimeoutException, NoSuchElementException):
            return False

    def is_clickable(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator))
            return True
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException):
            return False

    def is_present(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator))
            return True
        except (TimeoutException, NoSuchElementException):
            return False
        
    def is_alert_present(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            return True
        except TimeoutException:
            return False

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()  # Dismiss the alert after retrieving the text
        return alert_text