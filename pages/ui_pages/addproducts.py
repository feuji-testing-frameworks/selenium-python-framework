from actions.ui_actions import UI_Actions
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ProductsAddToCart(UI_Actions):
    phones_btn=(By.XPATH,"//a[@id='itemc' and @onclick='byCat('phone')' and contains(@class, 'list-group-item')]")

    samsung_mobile_link=(By.XPATH,"//a[text()='Samsung galaxy s6']")
    add_to_cart_btn=(By.XPATH,"//a[text()='Add to cart']")
    home_btn=(By.XPATH,"//a[text()='Home ']")
    select_laptop=(By.XPATH,"//a[text()='Sony vaio i5']")
    cart_btn=(By.ID,"cartur")
    delete_btn=(By.XPATH,"(//a[text()='Delete'])[2]")
    place_order_btn=(By.XPATH, "//button[text()='Place Order']")

    enter_name=(By.ID,"name")
    enter_country=(By.ID,"country")
    enter_city=(By.ID,"city")
    enter_card_details=(By.ID,"card")
    enter_month=(By.ID,"month")
    enter_year=(By.ID,"year")
    purchase_btn=(By.XPATH,"//button[text()='Purchase']")

    def __init__(self,driver):
            super().__init__(driver)

    def select_phone(self):
        time.sleep(2);
        # self.webElement_click(self.phones_btn)
        self.webElement_click(self.samsung_mobile_link)

    def phone_add_to_cart(self):
        self.webElement_click(self.add_to_cart_btn);
        expected_alert_message="Product added."
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            
            print("Alert message: ", alert_text)
            print("type of alert text: ",type(alert_text))
            assert alert_text == expected_alert_message, f"Actual alert message: '{alert_text}' does not match expected: '{expected_alert_message}'"
            alert.accept() 
        except TimeoutException:
            assert False, "Alert not present after adding laptop to cart"
    
    def laptop_add_to_cart(self):
        self.webElement_click(self.home_btn)
        self.webElement_click(self.select_laptop)
        self.webElement_click(self.add_to_cart_btn)
        expected_alert_message="Product added."
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print("Alert message: ", alert_text)
            assert alert_text == expected_alert_message, f"Actual alert message: '{alert_text}' does not match expected: '{expected_alert_message}'"
            alert.accept() 
        except TimeoutException:
            assert False, "Alert not present after adding laptop to cart"

    def delete_product_from_cart(self):
        time.sleep(1)
        self.webElement_click(self.cart_btn);
        self.webElement_click(self.delete_btn)
        time.sleep(3)
    def place_order_fill_details(self, name,country,city,card, month,year):
        self.webElement_click(self.place_order_btn)
        self.webElement_input(self.enter_name,name)
        self.webElement_input(self.enter_country,country)
        self.webElement_input(self.enter_city,city)
        self.webElement_input(self.enter_card_details,card)
        self.webElement_input(self.enter_month,month)
        self.webElement_input(self.enter_year,year)
        self.webElement_click(self.purchase_btn)






    


