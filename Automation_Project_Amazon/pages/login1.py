from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_user(self, username1):
        user_name1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "ap_email_login")))

        user_name1.send_keys(username1)
        user_name1.send_keys(Keys.ENTER)

    def login_password(self, password):
        password1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='ap_password']")))

        password1.send_keys(password)
        password1.send_keys(Keys.ENTER)