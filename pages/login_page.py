from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = driver.find_element(By.ID, "email")
        self.password_input = driver.find_element(By.ID, "password")
        self.login_button = driver.find_element(By.XPATH, "//input[@id='login']")

    def login(self, username, password):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_button.click()

    def is_logged_in(self):
        try:
            self.driver.find_element(By.XPATH, "//body/aside[@id='left_header_menu']/div[@id='wrapper']/ul[1]/li[1]/a[1]")
            return True
        except:
            return False
