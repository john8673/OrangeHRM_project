import time
from selenium.webdriver.common.by import By


class Login_Page:
    def __init__(self, driver):
        self.login_page_driver = driver
        self.username_textbox_locator = "username"
        self.password_textbox_locator = "password"
        self.login_button_locator = "//button[@type='submit']"
        self.invalid_credentials_locator = "//p[text()='Invalid credentials']"
        self.required_text_locator = "//span[text()='Required']"
        self.forgot_password_link_locator = "//p[text()='Forgot your password? ']"
        self.forgot_password_page_text = "//h6[text()='Reset Password']"
        self.orangehrm_mainpage_locator = "//a[text()='OrangeHRM, Inc']"
        self.linkedin_hyperlink_locator = "//a[@href='https://www.linkedin.com/company/orangehrm/mycompany/']"
        self.facebook_hyperlink_locator = "//a[@href='https://www.facebook.com/OrangeHRM/']"
        self.twitter_hyperlink_locator = "//a[@href='https://twitter.com/orangehrm?lang=en']"
        self.youtube_hyperlink_locator = "//a[@href='https://www.youtube.com/c/OrangeHRMInc']"

    def enter_username(self, username_text):
        self.login_page_driver.find_element(By.NAME, self.username_textbox_locator).send_keys(username_text)

    def enter_password(self, password_text):
        self.login_page_driver.find_element(By.NAME, self.password_textbox_locator).send_keys(password_text)

    def login_button_click(self):
        self.login_page_driver.find_element(By.XPATH, self.login_button_locator).click()

    def invalid_credentials_present(self):
        self.login_page_driver.find_element(By.XPATH, self.invalid_credentials_locator)
        return True

    def required_text_check(self):
        self.login_page_driver.find_element(By.XPATH, self.required_text_locator)
        return True

    def forgot_password_link_click(self):
        self.login_page_driver.find_element(By.XPATH, self.forgot_password_link_locator).click()

    def forgot_password_page(self):
        self.login_page_driver.find_element(By.XPATH, self.forgot_password_page_text)
        return True

    def orangehrm_mainpage_click(self):
        self.login_page_driver.find_element(By.XPATH, self.orangehrm_mainpage_locator).click()
        list_of_windows = self.login_page_driver.window_handles
        self.login_page_driver.switch_to.window(list_of_windows[1])
        if self.login_page_driver.title == "OrangeHRM HR Software | OrangeHRM":
            return True

    def linkedin_hyperlink_click(self):
        self.login_page_driver.find_element(By.XPATH, self.linkedin_hyperlink_locator).click()
        list_of_windows = self.login_page_driver.window_handles
        self.login_page_driver.switch_to.window(list_of_windows[1])
        if self.login_page_driver.title == "OrangeHRM | LinkedIn":
            return True
        self.login_page_driver.close()

    def facebook_hyperlink_click(self):
        self.login_page_driver.find_element(By.XPATH, self.facebook_hyperlink_locator).click()
        list_of_windows = self.login_page_driver.window_handles
        self.login_page_driver.switch_to.window(list_of_windows[1])
        self.login_page_driver.find_element(By.XPATH, "//div[@aria-label='Close']/i").click()
        if self.login_page_driver.title == "OrangeHRM - World's Most Popular Opensource HRIS | Secaucus NJ | Facebook":
            return True
        self.login_page_driver.close()

    def twitter_hyperlink_click(self):
        self.login_page_driver.find_element(By.XPATH, self.twitter_hyperlink_locator).click()
        list_of_windows = self.login_page_driver.window_handles
        self.login_page_driver.switch_to.window(list_of_windows[1])
        # WebDriverWait(self.login_page_driver, 10).until(expected_conditions.presence_of_element_located
        # ((By.XPATH, "//span[text()='Follow']")))
        # Used time.sleep as explicit wait didn't work
        time.sleep(10)
        # previously the twitter page had the title "OrangeHRM (@orangehrm) / X", it is now changed
        if self.login_page_driver.title == "Log in to X / X":
            return True

    def youtube_hyperlink_click(self):
        self.login_page_driver.find_element(By.XPATH, self.youtube_hyperlink_locator).click()
        list_of_windows = self.login_page_driver.window_handles
        self.login_page_driver.switch_to.window(list_of_windows[1])
        # Used time.sleep as explicit wait didn't work
        time.sleep(5)
        if self.login_page_driver.title == "OrangeHRM Inc - YouTube":
            return True
