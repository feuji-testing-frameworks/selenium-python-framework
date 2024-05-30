from actions.mobile_actions import Appium_Actions
from appium.webdriver.common.appiumby import AppiumBy

class ClickAllNavigationButtons(Appium_Actions) :

    remind_me_later_button = (AppiumBy.XPATH , "//android.widget.Button[@resource-id='android:id/button2']");

    def __init__(self, driver):
        super().__init__(driver);
    
    def click_on_remindmelater_button(self) :
        self.click_webelement(self.remind_me_later_button);

    def click_on_navigation_elements(self,element) :
        # self.click_webelement(self.remind_me_later_button);
        if element == "Activity" :
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@content-desc='Activity']/android.widget.FrameLayout").click();
        else :
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@content-desc='"+ element +"']").click();