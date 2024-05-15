import pytest
import time
from tests.conftest import appium_driver_setup
from pages.mobile_pages.loginpage import LoginPage
from pages.mobile_pages.addrecipepage import Add_Recipe_Page
from pages.mobile_pages.moreoptionsvalidation import MoreOptionsValidations
from pages.mobile_pages.searchpage import SearchPage
from pages.mobile_pages.clickallheaderelements import ClickAllNavigationButtons

class TestMobileApp :

    @pytest.mark.run(order = 1)
    def test_login_functionality(self,appium_driver_setup,mobile_data) :
        driver = appium_driver_setup
        loginPage = LoginPage(driver);
        loginPage.login_function( mobile_data['username'], mobile_data['password']);
        loginPage.logout_function();
    
    @pytest.mark.run(order = 2)
    def test_more_options_validation(self,appium_driver_setup,mobile_data) :
        driver = appium_driver_setup
        loginPage = LoginPage(driver);
        loginPage.login_function( mobile_data['username'], mobile_data['password']);
        moreOptions = MoreOptionsValidations(driver);
        moreOptions.clickOnMoreOptions();
        for element in mobile_data['moreoptions'] :
            time.sleep(3);
            assert moreOptions.moreoptions_validation(element) == True , f"{element} is not displayed";
        moreOptions.clickOnAppUpdate();
        loginPage.logout_function();
    
    @pytest.mark.run(order = 3)
    def test_search_functionality(self,appium_driver_setup,mobile_data) :
        driver = appium_driver_setup
        loginPage = LoginPage(driver);
        loginPage.login_function(mobile_data['username'], mobile_data['password']);
        searchPage = SearchPage(driver);
        searchPage.search_function(mobile_data['searchdata']);
        loginPage.logout_function();

    @pytest.mark.run(order = 4)
    def test_add_recipe_functionality(self,appium_driver_setup,mobile_data) :
        driver = appium_driver_setup
        loginPage = LoginPage(driver);
        loginPage.login_function(mobile_data['username'], mobile_data['password']);
        addRecipePage = Add_Recipe_Page(driver);
        addRecipePage.add_recipe_function(mobile_data['title'],mobile_data['ingredients'],mobile_data['instructions']);
        loginPage.logout_function();

    @pytest.mark.run(order = 5)
    def test_click_navBar_elements(self,appium_driver_setup,mobile_data) :
        driver = appium_driver_setup
        loginPage = LoginPage(driver);
        loginPage.login_function(mobile_data['username'],mobile_data['password']);
        navBarElement = ClickAllNavigationButtons(driver);
        for element in mobile_data['navigationbar'] :
            navBarElement.click_on_navigation_elements(element);
        loginPage.logout_function();
