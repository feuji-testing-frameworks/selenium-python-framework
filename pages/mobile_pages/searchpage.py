from actions.mobile_actions import Appium_Actions
from appium.webdriver.common.appiumby import AppiumBy

class SearchPage(Appium_Actions) :

    search_button = (AppiumBy.XPATH , "//android.widget.Button[@content-desc='Search All Recipes']");
    search_input = (AppiumBy.XPATH , "//android.widget.AutoCompleteTextView[@resource-id='com.bigoven.android:id/searchBarText']");
    back_button = (AppiumBy.XPATH , "//android.widget.ImageButton[@content-desc='Navigate up']");

    def __init__(self, driver) :
        super().__init__(driver);

    def search_function(self, searchText) :
        self.click_webelement(self.search_button);
        self.click_webelement(self.search_input);
        self.input_webelement(self.search_input , searchText);
        self.driver.execute_script('mobile: performEditorAction', {'action': 'search'});
        self.click_webelement(self.back_button);