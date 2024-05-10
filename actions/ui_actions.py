from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UI_Actions :

    """Intilize the webdriver"""
    def __init__(self,driver) :
        self.driver = driver;

    """This function is used for clicking the web element"""
    def webElement_click(self,locator) :
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).click();

    """This function is used for entering the text into the web element"""
    def webElement_input(self,locator,text) :
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).send_keys(text);

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
