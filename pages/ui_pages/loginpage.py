from actions.ui_actions import UI_Actions
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class DemoBlazeLoginPage(UI_Actions):
     
    menu_login=(By.ID,"login2")
    username_field=(By.ID,"loginusername")
    password_field=(By.ID,"loginpassword")
    login_btn=(By.XPATH,"//button[text()='Log in']")
    logout_btn=(By.XPATH,"//a[@id='logout2']")

    cancel_login=(By.XPATH,"(//span[@aria-hidden='true'][text()='×'])[3]")

    def __init__(self,driver):
            super().__init__(driver)

    def navigate_to_login(self):
        time.sleep(3)
        self.webElement_click(self.menu_login)
    
    def enter_credentials(self, username,password):
        self.webElement_input(self.username_field, username)
        self.webElement_input(self.password_field, password)

    def click_on_signin(self):
        self.webElement_click(self.login_btn)
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            pass
        

    def login_demo_blaze(self, username, password):
        self.webElement_click(self.menu_login)
        self.webElement_input(self.username_field, username)
        self.webElement_input(self.password_field, password)
        self.webElement_click(self.login_btn)
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            pass
        time.sleep(3)
    def logout(self):
         self.webElement_click(self.logout_btn)
        
    def login_invalid_credentials(self, username, incorrect_password):
        expected_alert_message="Wrong password."
        self.webElement_click(self.menu_login)
        time.sleep(3)
        self.webElement_input(self.username_field, username)
        self.webElement_input(self.password_field, incorrect_password)
        self.webElement_click(self.login_btn)
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print("Alert message: ", alert_text)
            assert alert_text == expected_alert_message, f"Actual alert message: '{alert_text}' does not match expected: '{expected_alert_message}'"
            alert.accept()  
        except TimeoutException:
            print("No alert found within the timeout.")
        
        self.webElement_click(self.cancel_login)
        time.sleep(2)
        
