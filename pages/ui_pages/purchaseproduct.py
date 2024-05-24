from actions.ui_actions import UI_Actions
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class PurchaseProductPage(UI_Actions):
   
    monitors_btn=(By.XPATH,"//a[text()='Monitors']")
    select_apple_monitor=(By.XPATH,"//a[text()='Apple monitor 24']")
    add_to_cart_btn=(By.XPATH,"//a[text()='Add to cart']")

    cart_btn=(By.ID,"cartur")
   
    place_order_btn=(By.XPATH, "//button[text()='Place Order']")

    enter_name=(By.ID,"name")
    enter_country=(By.ID,"country")
    enter_city=(By.ID,"city")
    enter_card_details=(By.ID,"card")
    enter_month=(By.ID,"month")
    enter_year=(By.ID,"year")
    purchase_btn=(By.XPATH,"//button[text()='Purchase']")
    ok_order_btn=(By.XPATH,"//button[text()='OK']")

    def __init__(self,driver):
            super().__init__(driver)

    def select_monitor(self):
        time.sleep(1);
        # self.webElement_click(self.phones_btn)
        self.webElement_click(self.monitors_btn)
        self.webElement_click(self.select_apple_monitor)

    def monitor_add_to_cart(self):
        self.webElement_click(self.add_to_cart_btn);
        expected_alert_message="Product added."
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print("Alert message: ", alert_text)
            assert alert_text == expected_alert_message, f"Actual alert message: '{alert_text}' does not match expected: '{expected_alert_message}'"
            alert.accept() 
        except TimeoutException:
            pass
    def goto_cart(self):
        self.webElement_click(self.cart_btn)
        self.webElement_click(self.place_order_btn)

    def place_order_fill_details(self, name,country,city,card, month,year):
        
        self.webElement_input(self.enter_name,name)
        entered_name = self.driver.find_element(*self.enter_name).get_attribute("value")

        assert entered_name == "demouser1", f"Entered name '{entered_name}' does not match expected name '{name}'"
        self.webElement_input(self.enter_country,country)
        self.webElement_input(self.enter_city,city)
        self.webElement_input(self.enter_card_details,card)
        self.webElement_input(self.enter_month,month)
        self.webElement_input(self.enter_year,year)
        self.webElement_click(self.purchase_btn)
        time.sleep(1)
        self.webElement_click(self.ok_order_btn)