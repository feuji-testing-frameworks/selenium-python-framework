from appium.webdriver.webdriver import WebDriver

class Appium_Actions :

    def __init__(self,driver,implicit_wait_time = 10) :
        self.driver = driver;
        self.driver.implicitly_wait(implicit_wait_time);

    def webElement(self,locator) :
        element = self.driver.find_element(* locator);
        return element;

    def click_webelement(self,locator) :
        self.webElement(locator).click();

    def input_webelement(self,locator,text) :
        self.webElement(locator).send_keys(text);

    def get_webelement_text(self,locator) :
        return self.webElement(locator).text;

    def scroll_to_element(self,locator) :
        self.driver.execute_script("window.scrollBy(0, arguments[0].offsetTop);", locator);
    
    def is_webelement_displayed(self,locator) :
        return self.webElement(locator).is_displayed();
