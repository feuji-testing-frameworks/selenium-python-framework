from actions.ui_actions import UI_Actions
from selenium.webdriver.common.by import By
import time

class LumaLoginPage(UI_Actions):
     
    signin_menu_btn=(By.XPATH, "(//a[contains(text(), 'Sign In')])[1]")   
    input_field=(By.ID,"email")
    password_field=(By.XPATH,"//input[@title='Password']")
    sign_in_btn=(By.XPATH,"//button[@class='action login primary']")

    def __init__(self,driver):
            super().__init__(driver)

    def navigate_to_login(self):
        time.sleep(3)
        self.webElement_click(self.signin_menu_btn)
    
    def enter_credentials(self, email,password):
        self.webElement_input(self.input_field, email)
        self.webElement_input(self.password_field, password)

    def click_on_signin(self):
        self.webElement_click(self.sign_in_btn)
         
