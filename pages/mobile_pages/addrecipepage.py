from actions.mobile_actions import Appium_Actions
from appium.webdriver.common.appiumby import AppiumBy
import time

class Add_Recipe_Page(Appium_Actions) :

    my_recipe_button = (AppiumBy.XPATH, "//android.widget.LinearLayout[@content-desc='My Recipes']/android.widget.TextView");
    add_recipe_button = (AppiumBy.XPATH, "//android.widget.ImageButton[@resource-id='com.bigoven.android:id/fab']");
    type_in_recipie_button = (AppiumBy.XPATH , "//android.widget.LinearLayout[@resource-id='com.bigoven.android:id/type_it_in_fab']");
    title_input = (AppiumBy.XPATH , "//android.widget.EditText[@resource-id='titleInput']");
    ingredients_input = (AppiumBy.XPATH , "//android.widget.EditText[@resource-id='ingredientsInput']");
    instructions_input = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='instructionsInput']");
    add_Button = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='submitBtn']");
    back_navigation_button = (AppiumBy.XPATH, "//android.view.ViewGroup[@resource-id='com.bigoven.android:id/appToolbar']/android.widget.ImageButton");
    remind_me_later_button = (AppiumBy.XPATH , "//android.widget.Button[@resource-id='android:id/button2']");

    def __init__(self, driver):
        super().__init__(driver);
    
    def click_on_remindmelater_button(self) :
        self.click_webelement(self.remind_me_later_button);

    def add_recipe_function(self,title,ingredients,instructions) :
        # self.click_webelement(self.remind_me_later_button);
        self.click_webelement(self.my_recipe_button);
        self.click_webelement(self.add_recipe_button);
        self.click_webelement(self.type_in_recipie_button);
        self.input_webelement(self.title_input,title);
        time.sleep(3);
        self.input_webelement(self.ingredients_input,ingredients);
        time.sleep(3);
        self.input_webelement(self.instructions_input,instructions);
        self.click_webelement(self.add_Button);
        self.click_webelement(self.back_navigation_button);
