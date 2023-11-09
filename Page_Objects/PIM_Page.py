from selenium.webdriver.common.by import By


class PIM_Page:
    def __init__(self, driver):
        self.pim_page_driver = driver
        self.pim_page_locator = "//a[@href='/web/index.php/pim/viewPimModule']"
        self.add_employee_button_locator = "//button[text()=' Add ']"
        self.edit_employee_button_locator = "//div[@class='oxd-table-body']/div[1]/div/div[9]/div/button[2]"
        self.delete_employee_button_locator = "//div[@class='oxd-table-body']/div[1]/div/div[9]/div/button[1]"
        self.confirm_delete_button_locator = "//button[text()=' Yes, Delete ']"
        self.first_name_textbox_locator = "firstName"
        self.middle_name_textbox_locator = "middleName"
        self.last_name_textbox_locator = "lastName"
        self.pim_page_save_button_locator = "//button[text()=' Save ']"
        self.nickname_textbox_locator = "//label[text()='Nickname']/parent::div/following-sibling::div/child::input"
        self.other_id_textbox_locator = "//label[text()='Other Id']/parent::div/following-sibling::div/child::input"

        # (//label[text()="Driver's License Number"]/parent::div/following-sibling::div) -- this XPath has issues with
        # both single and double quotes. Had to use absolute XPath.

        self.driver_license_number_locator = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
        self.license_expiry_date_locator = "//label[text()='License Expiry Date']/parent::div/following-sibling::div/child::div/child::div/child::input"
        self.ssn_number_textbox_locator = "//label[text()='SSN Number']/parent::div/following-sibling::div/child::input"
        self.sin_number_textbox_locator = "//label[text()='SIN Number']/parent::div/following-sibling::div/child::input"
        self.nationality_dropdown_locator = "//label[text()='Nationality']/parent::div/following-sibling::div/child::div"
        self.marital_status_dropdown_locator = "//label[text()='Marital Status']/parent::div/following-sibling::div/child::div"
        self.dob_locator = "//label[text()='Date of Birth']/parent::div/following-sibling::div/child::div/child::div/child::input"
        self.gender_radio_button_locator = "//label[text()='Male']"
        self.military_service_textbox_locator = "//label[text()='Military Service']/parent::div/following-sibling::div/child::input"
        self.smoker_checkbox_locator = "//label[text()='Yes']"
        self.blood_type_dropdown_locator = "//label[text()='Blood Type']/parent::div/following-sibling::div/child::div"
        self.details_page_save_button_locator = "//div[@class='oxd-form-actions']/child::p/parent::div/child::button"
        self.success_message_locator = "//p[text()='Success']"

    def pim_page_click(self):
        self.pim_page_driver.find_element(By.XPATH, self.pim_page_locator).click()

    def add_employee_button_click(self):
        self.pim_page_driver.find_element(By.XPATH, self.add_employee_button_locator).click()

    def edit_employee_button_click(self):
        self.pim_page_driver.find_element(By.XPATH, self.edit_employee_button_locator).click()

    def delete_employee_button_click(self):
        self.pim_page_driver.find_element(By.XPATH, self.delete_employee_button_locator).click()

    def confirm_delete_button_click(self):
        self.pim_page_driver.find_element(By.XPATH, self.confirm_delete_button_locator).click()

    def enter_first_name(self, first_name_text):
        self.pim_page_driver.find_element(By.NAME, self.first_name_textbox_locator).send_keys(first_name_text)

    def enter_middle_name(self, middle_name_text):
        self.pim_page_driver.find_element(By.NAME, self.middle_name_textbox_locator).send_keys(middle_name_text)

    def enter_last_name(self, last_name_text):
        self.pim_page_driver.find_element(By.NAME, self.last_name_textbox_locator).send_keys(last_name_text)

    def pim_page_save_button_click(self):
        self.pim_page_driver.find_element(By.XPATH, self.pim_page_save_button_locator).click()

    def enter_nickname(self):
        self.pim_page_driver.find_element(By.XPATH, self.nickname_textbox_locator).send_keys("Nil")

    def enter_other_id(self):
        self.pim_page_driver.find_element(By.XPATH, self.other_id_textbox_locator).send_keys("Nil")

    def enter_driving_license_number(self, dl_number):
        self.pim_page_driver.find_element(By.XPATH, self.driver_license_number_locator).send_keys(dl_number)

    def enter_license_expiry_date(self, dl_expiry_date):
        self.pim_page_driver.find_element(By.XPATH, self.license_expiry_date_locator).send_keys(dl_expiry_date)

    def enter_ssn_number(self, ssn_number):
        self.pim_page_driver.find_element(By.XPATH, self.ssn_number_textbox_locator).send_keys(ssn_number)

    def enter_sin_number(self, sin_number):
        self.pim_page_driver.find_element(By.XPATH, self.sin_number_textbox_locator).send_keys(sin_number)

    def enter_nationality(self):
        self.pim_page_driver.find_element(By.XPATH, self.nationality_dropdown_locator).click()

    def enter_marital_status(self):
        self.pim_page_driver.find_element(By.XPATH, self.marital_status_dropdown_locator).click()

    def enter_dob(self, dob):
        self.pim_page_driver.find_element(By.XPATH, self.dob_locator).send_keys(dob)

    def click_your_gender(self):
        self.pim_page_driver.find_element(By.XPATH, self.gender_radio_button_locator).click()

    def enter_military_service(self):
        self.pim_page_driver.find_element(By.XPATH, self.military_service_textbox_locator).send_keys("No")

    def click_smoker_checkbox(self):
        self.pim_page_driver.find_element(By.XPATH, self.smoker_checkbox_locator).click()

    def enter_blood_type(self):
        self.pim_page_driver.find_element(By.XPATH, self.blood_type_dropdown_locator).click()

    def details_page_save_button_click(self):
        self.pim_page_driver.find_element(By.XPATH, self.details_page_save_button_locator).click()

    def success_message_check(self):
        self.pim_page_driver.find_element(By.XPATH, self.success_message_locator)
        return True

