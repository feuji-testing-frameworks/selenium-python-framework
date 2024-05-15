from actions.mobile_actions import Appium_Actions
from appium.webdriver.common.appiumby import AppiumBy

class ClickAllNavigationButtons(Appium_Actions) :

    def __init__(self, driver):
        super().__init__(driver);

    def click_on_navigation_elements(self,element) :
        if element == "Activity" :
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@content-desc='Activity']/android.widget.FrameLayout").click();
        else :
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@content-desc='"+ element +"']").click();