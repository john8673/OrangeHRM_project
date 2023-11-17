
import json
from selenium import webdriver
import unittest

from selenium.webdriver import ActionChains, Keys

from Page_Objects.PIM_Page import PIM_Page
from Page_Objects.Login_Page import Login_Page
from Page_Objects.Dashboard_Page import Dashboard_Page


class PIMPageTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.chrome_driver = webdriver.Chrome()
        self.chrome_driver.maximize_window()
        self.chrome_driver.implicitly_wait(20)
        self.chrome_driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        self.open_file1 = open("C:\\Automation testing\\AT18\\Project_one\\Test_Data\\test_data.json")
        self.json_dict = json.load(self.open_file1)
        lp_object = Login_Page(self.chrome_driver)
        lp_object.enter_username(self.json_dict.get("valid_username"))
        lp_object.enter_password(self.json_dict.get("valid_password"))
        lp_object.login_button_click()
        pp_object = PIM_Page(self.chrome_driver)
        pp_object.pim_page_click()

    def test_add_new_employee(self):
        pp_object = PIM_Page(self.chrome_driver)
        pp_object.add_employee_button_click()
        pp_object.enter_first_name(self.json_dict.get("first_name"))
        pp_object.enter_middle_name(self.json_dict.get("middle_name"))
        pp_object.enter_last_name(self.json_dict.get("last_name"))
        pp_object.pim_page_save_button_click()
        pp_object.enter_nickname()
        pp_object.enter_other_id()
        pp_object.enter_driving_license_number(self.json_dict.get("dl_number"))
        pp_object.enter_license_expiry_date(self.json_dict.get("dl_expiry_date"))
        pp_object.enter_ssn_number(self.json_dict.get("ssn_number"))
        pp_object.enter_sin_number(self.json_dict.get("sin_number"))
        action = ActionChains(self.chrome_driver)
        pp_object.enter_nationality()
        action.key_down(Keys.DOWN).key_down(Keys.DOWN).key_down(Keys.DOWN).key_down(Keys.DOWN).perform()
        pp_object.enter_marital_status()
        action.key_down(Keys.DOWN).perform()
        pp_object.enter_dob(self.json_dict.get("dob"))
        pp_object.click_your_gender()
        pp_object.enter_military_service()
        pp_object.click_smoker_checkbox()
        pp_object.enter_blood_type()
        action.key_down(Keys.DOWN).key_down(Keys.DOWN).perform()
        pp_object.details_page_save_button_click()
        assert pp_object.success_message_check()

    def test_edit_existing_employee(self):
        pp_object = PIM_Page(self.chrome_driver)
        pp_object.edit_employee_button_click()
        pp_object.enter_driving_license_number(self.json_dict.get("dl_number"))
        pp_object.details_page_save_button_click()
        assert pp_object.success_message_check()

    def test_delete_existing_employee(self):
        pp_object = PIM_Page(self.chrome_driver)
        pp_object.delete_employee_button_click()
        pp_object.confirm_delete_button_click()
        assert pp_object.success_message_check()

    def tearDown(self) -> None:
        dp_object = Dashboard_Page(self.chrome_driver)
        dp_object.account_dropdown_click()
        dp_object.logout_button_click()
