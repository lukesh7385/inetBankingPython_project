from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.XPATH, "//input[@name='uid' and @type='text']")
        self.password_input = (By.XPATH, "//input[@name='password']")
        self.submit_button = (By.XPATH, "//input[@name='btnLogin']")
        self.logout_button = (By.XPATH, "//a[normalize-space()='Log out']")

    def setUserName(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(*self.submit_button).click()

    def clickLogout(self):
        self.driver.find_element(*self.logout_button).click()

    def is_logged_in(self):
        return self.driver.find_element(*self.submit_button).is_displayed()
