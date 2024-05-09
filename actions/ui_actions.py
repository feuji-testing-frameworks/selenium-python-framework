from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UI_Actions :

    def __init__(self,driver) :
        self.driver = driver;

    def webElement_click(self,locator) :
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).click();

    def webElement_input(self,locator,text) :
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).send_keys(text);

    def webElement_text(self,locator) :
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).text;

    def scroll_to_element(self,locator) :
        self.driver.execute_script("window.scrollBy(0, arguments[0].offsetTop);", locator);
        WebDriverWait(self.driver,self.get_wait_time()).until(EC.visibility_of_element_located(locator));

    def webElement_isDisplayed(self,locator) :
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).is_displayed();

    def webElement_input_clear(self,locator) :
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).clear();
