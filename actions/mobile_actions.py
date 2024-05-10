from appium.webdriver.webdriver import WebDriver

class Appium_Actions :

    """This function is used for intilizing the driver"""
    def __init__(self,driver,implicit_wait_time = 10) :
        self.driver = driver;
        self.driver.implicitly_wait(implicit_wait_time);

    """This function is used for returing the element"""
    def webElement(self,locator) :
        element = self.driver.find_element(* locator);
        return element;

    """This function is used for clicking the web element"""
    def click_webelement(self,locator) :
        self.webElement(locator).click();

    """This function is used for entering the text into the web element"""
    def input_webelement(self,locator,text) :
        self.webElement(locator).send_keys(text);

    """This function is used for entering the text into the web element"""
    def get_webelement_text(self,locator) :
        return self.webElement(locator).text;

    """This function is used for scrolling the web element"""
    def scroll_to_element(self,locator) :
        self.driver.execute_script("window.scrollBy(0, arguments[0].offsetTop);", locator);
    
    """This function is used for checking the web element is displayed or not"""
    def is_webelement_displayed(self,locator) :
        return self.webElement(locator).is_displayed();
