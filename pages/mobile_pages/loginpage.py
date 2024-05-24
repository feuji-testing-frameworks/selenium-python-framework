from actions.mobile_actions import Appium_Actions
from appium.webdriver.common.appiumby import AppiumBy

class LoginPage(Appium_Actions) :

    signin_button = (AppiumBy.XPATH , "//android.widget.TextView[@text='Sign in']");
    email_input = (AppiumBy.XPATH , "//android.widget.EditText[@resource-id='com.bigoven.android:id/email']");
    password_input = (AppiumBy.XPATH , "//android.widget.EditText[@resource-id='com.bigoven.android:id/password']");
    getIdeasElement = (AppiumBy.XPATH , "//android.widget.LinearLayout[@content-desc='Get Ideas']/android.widget.TextView")
    more_options_button = (AppiumBy.XPATH , "//android.widget.ImageView[@content-desc='More options']");
    settings_button = (AppiumBy.XPATH , "//android.widget.TextView[@text = 'Settings']");
    signout_button = (AppiumBy.XPATH , "//android.widget.TextView[@text='Sign Out']");
    confirm_signout_button = (AppiumBy.XPATH , "//android.widget.Button[@resource-id='android:id/button1']");

    def __init__(self, driver) :
        super().__init__(driver);

    def login_function(self,username,password) :
        self.click_webelement(self.signin_button);
        self.input_webelement(self.email_input, username);
        self.input_webelement(self.password_input, password);
        self.click_webelement(self.signin_button);

    def logout_function(self) :
        self.click_webelement(self.more_options_button);
        self.click_webelement(self.settings_button);
        self.click_webelement(self.signout_button);
        self.click_webelement(self.confirm_signout_button);
