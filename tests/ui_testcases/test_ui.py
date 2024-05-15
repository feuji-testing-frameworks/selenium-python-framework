from pages.ui_pages.loginpage import LumaLoginPage
import pytest

@pytest.mark.usefixtures("browser_setup")
class TestUiLuma:

    # @pytest.mark.run()
    def test_login_test(self,ui_data):
        self.luma_login_page= LumaLoginPage(self.driver)
        self.luma_login_page.navigate_to_login()
        self.luma_login_page.enter_credentials(ui_data['email'],ui_data['password'])
        self.luma_login_page.click_on_signin()

