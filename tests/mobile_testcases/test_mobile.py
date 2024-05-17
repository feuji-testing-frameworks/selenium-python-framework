import pytest
import time
import logging
from tests.conftest import appium_driver_setup
from pages.mobile_pages.loginpage import LoginPage
from pages.mobile_pages.addrecipepage import Add_Recipe_Page
from pages.mobile_pages.moreoptionsvalidation import MoreOptionsValidations
from pages.mobile_pages.searchpage import SearchPage
from pages.mobile_pages.clickallheaderelements import ClickAllNavigationButtons

class TestMobileApp :

    """Login with valid username and password"""
    @pytest.mark.run(order = 1)
    def test_login_functionality(self,appium_driver_setup,mobile_data) :
        logging.getLogger("root").info("Starting the test_login_functionality")
        driver = appium_driver_setup
        loginPage = LoginPage(driver);
        loginPage.login_function( mobile_data['username'], mobile_data['password']);
        logging.getLogger("root").info("Login Successful")
        loginPage.logout_function();
        logging.getLogger("root").info("Logout Successful")
    
    """Validate the elements present in the more options or not"""
    @pytest.mark.run(order = 2)
    def test_more_options_validation(self,appium_driver_setup,mobile_data) :
        logging.getLogger("root").info("Starting the test_more_options_validation")
        driver = appium_driver_setup
        loginPage = LoginPage(driver);
        loginPage.login_function( mobile_data['username'], mobile_data['password']);
        logging.getLogger("root").info("Login Successful")
        moreOptions = MoreOptionsValidations(driver);
        moreOptions.clickOnMoreOptions();
        for element in mobile_data['moreoptions'] :
            time.sleep(3);
            assert moreOptions.moreoptions_validation(element) == True , f"{element} is not displayed";
        logging.getLogger("root").info("Verifying the elements present in the moreOptions")
        moreOptions.clickOnAppUpdate();
        logging.getLogger("root").info("Click on App Update")
        loginPage.logout_function();
        logging.getLogger("root").info("Logout Successful")
    
    """Checking the Search Functionality"""
    @pytest.mark.run(order = 3)
    def test_search_functionality(self,appium_driver_setup,mobile_data) :
        logging.getLogger("root").info("Starting the test_search_functionality")
        driver = appium_driver_setup
        loginPage = LoginPage(driver);
        loginPage.login_function(mobile_data['username'], mobile_data['password']);
        logging.getLogger("root").info("Login Successful")
        searchPage = SearchPage(driver);
        searchPage.search_function(mobile_data['searchdata']);
        logging.getLogger("root").info("Searching Functionality")
        loginPage.logout_function();
        logging.getLogger("root").info("Logout Successful")

    """Add the own recipe in addRecipe section"""
    @pytest.mark.run(order = 4)
    def test_add_recipe_functionality(self,appium_driver_setup,mobile_data) :
        logging.getLogger("root").info("Starting the test_add_recipe_functionality")
        driver = appium_driver_setup
        loginPage = LoginPage(driver);
        loginPage.login_function(mobile_data['username'], mobile_data['password']);
        logging.getLogger("root").info("Login Successful")
        addRecipePage = Add_Recipe_Page(driver);
        addRecipePage.add_recipe_function(mobile_data['title'],mobile_data['ingredients'],mobile_data['instructions']);
        logging.getLogger("root").info("Add the recipe")
        loginPage.logout_function();
        logging.getLogger("root").info("Logout Successful")

    """Validate the elements present in the navBar"""
    @pytest.mark.run(order = 5)
    def test_click_navBar_elements(self,appium_driver_setup,mobile_data) :
        logging.getLogger("root").info("Starting the test_click_navBar_elements")
        driver = appium_driver_setup
        loginPage = LoginPage(driver);
        loginPage.login_function(mobile_data['username'],mobile_data['password']);
        logging.getLogger("root").info("Login Successful")
        navBarElement = ClickAllNavigationButtons(driver);
        for element in mobile_data['navigationbar'] :
            navBarElement.click_on_navigation_elements(element);
        logging.getLogger("root").info("Checking the Navigation bar elements")
        loginPage.logout_function();
        logging.getLogger("root").info("Logout Successful")
