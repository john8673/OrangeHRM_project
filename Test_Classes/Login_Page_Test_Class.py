import json
from selenium import webdriver
import unittest

from Page_Objects.Dashboard_Page import Dashboard_Page
from Page_Objects.Login_Page import Login_Page


class LoginPageTestCase(unittest.TestCase):
    chrome_driver = None

    def setUp(self) -> None:
        self.chrome_driver = webdriver.Chrome()
        self.chrome_driver.maximize_window()
        self.chrome_driver.implicitly_wait(20)
        self.chrome_driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        open_file1 = open("C:\\Automation testing\\AT18\\Eshwar_sessions\\Test_Data\\test_data.json")
        self.json_dict = json.load(open_file1)

    def test_successful_login(self):
        lp_object = Login_Page(self.chrome_driver)
        dp_object = Dashboard_Page(self.chrome_driver)
        lp_object.enter_username(self.json_dict.get("valid_username"))
        lp_object.enter_password(self.json_dict.get("valid_password"))
        lp_object.login_button_click()
        assert dp_object.is_dashboard_text_present()
        dp_object.account_dropdown_click()
        dp_object.logout_button_click()

    def test_invalid_username_and_no_password(self):
        lp_object = Login_Page(self.chrome_driver)
        lp_object.enter_username(self.json_dict.get("invalid_username"))
        lp_object.login_button_click()
        assert lp_object.required_text_check()

    def test_valid_username_and_no_password(self):
        lp_object = Login_Page(self.chrome_driver)
        lp_object.enter_username(self.json_dict.get("valid_username"))
        lp_object.login_button_click()
        assert lp_object.required_text_check()

    def test_invalid_password_and_no_username(self):
        lp_object = Login_Page(self.chrome_driver)
        lp_object.enter_password(self.json_dict.get("invalid_password"))
        lp_object.login_button_click()
        assert lp_object.required_text_check()

    def test_valid_password_and_no_username(self):
        lp_object = Login_Page(self.chrome_driver)
        lp_object.enter_password(self.json_dict.get("valid_password"))
        lp_object.login_button_click()
        assert lp_object.required_text_check()

    def test_valid_username_and_invalid_password(self):
        lp_object = Login_Page(self.chrome_driver)
        lp_object.enter_username(self.json_dict.get("valid_username"))
        lp_object.enter_password(self.json_dict.get("invalid_password"))
        lp_object.login_button_click()
        assert lp_object.invalid_credentials_present()

    def test_invalid_username_and_valid_password(self):
        lp_object = Login_Page(self.chrome_driver)
        lp_object.enter_username(self.json_dict.get("invalid_username"))
        lp_object.enter_password(self.json_dict.get("valid_password"))
        lp_object.login_button_click()
        assert lp_object.invalid_credentials_present()

    def test_invalid_username_and_invalid_password(self):
        lp_object = Login_Page(self.chrome_driver)
        lp_object.enter_username(self.json_dict.get("invalid_username"))
        lp_object.enter_password(self.json_dict.get("invalid_password"))
        lp_object.login_button_click()
        assert lp_object.invalid_credentials_present()

    def test_forgot_password_link(self):
        lp_object = Login_Page(self.chrome_driver)
        lp_object.forgot_password_link_click()
        assert lp_object.forgot_password_page()

    def test_orangehrm_mainpage_click(self):
        lp_object = Login_Page(self.chrome_driver)
        assert lp_object.orangehrm_mainpage_click()

    def test_linkedin_hyperlink_click(self):
        lp_object = Login_Page(self.chrome_driver)
        assert lp_object.linkedin_hyperlink_click()

    def test_facebook_hyperlink_click(self):
        lp_object = Login_Page(self.chrome_driver)
        assert lp_object.facebook_hyperlink_click()

    def test_twitter_hyperlink_click(self):
        lp_object = Login_Page(self.chrome_driver)
        assert lp_object.twitter_hyperlink_click()

    def test_youtube_hyperlink_click(self):
        lp_object = Login_Page(self.chrome_driver)
        assert lp_object.youtube_hyperlink_click()

