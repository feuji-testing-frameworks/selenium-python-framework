from pages.ui_pages.loginpage import DemoBlazeLoginPage
import pytest
from pages.ui_pages.addproducts import ProductsAddToCart
from pages.ui_pages.purchaseproduct import PurchaseProductPage
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import json

@pytest.mark.usefixtures("browser_setup","log_on_failure")
class TestUiDemoBlaze:

   # @pytest.mark.run()
    def test_login(self,ui_data):
        self.login_page= DemoBlazeLoginPage(self.driver)
        self.login_page.navigate_to_login()
        self.login_page.enter_credentials(ui_data['email'],ui_data['password'])
        self.login_page.click_on_signin()
        self.login_page.logout()

    def test_products_add_to_cart(self, ui_data):
        self.login_page= DemoBlazeLoginPage(self.driver)
        self.login_page.login_demo_blaze(ui_data['email'],ui_data['password'])
        self.products_page=ProductsAddToCart(self.driver)
        self.products_page.select_phone()
        self.products_page.phone_add_to_cart()
        self.products_page.laptop_add_to_cart()
        self.products_page.delete_product_from_cart()
        # self.products_page.place_order_fill_details(ui_data['name'],ui_data['country'],ui_data['city'],ui_data['card'],ui_data['year'],ui_data['month'])
        self.login_page.logout()

    def test_purchase_product(self,ui_data):
        self.login_page=DemoBlazeLoginPage(self.driver)
        self.login_page.login_demo_blaze(ui_data['email'],ui_data['password'])
        self.purchase_product_page=PurchaseProductPage(self.driver)
        self.purchase_product_page.select_monitor()
        self.purchase_product_page.monitor_add_to_cart()
        self.purchase_product_page.goto_cart()
        self.purchase_product_page.place_order_fill_details(ui_data['name'],ui_data['country'],ui_data['city'],ui_data['card'],ui_data['year'],ui_data['month'])
        self.login_page.logout()

    
    def test_veify_menu_items(self,ui_data):
        self.login_page=DemoBlazeLoginPage(self.driver)
        self.login_page.login_demo_blaze(ui_data['email'],ui_data['password'])
        with open('data/ui_data.json') as f:
            self.navbar_elements = json.load(f)["navbar"]

        for element_name in self.navbar_elements:
            time.sleep(2)
            try:
                sidebar_element = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, f"//a[text()='{element_name}']"))
                )
                assert sidebar_element.is_displayed(), f"{element_name} should be visible"
            except TimeoutException:
                assert False, f"{element_name} is not visible"
    
        time.sleep(3)
        self.login_page.logout()

    def test_invalid_credential_login(self,ui_data):
        self.login_page=DemoBlazeLoginPage(self.driver)
        self.login_page.login_invalid_credentials(ui_data['email'], ui_data['incorrect_password'])

    