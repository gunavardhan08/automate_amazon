from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Payment_Page:
    def __init__(self, driver):
        self.driver = driver

    def payment_check(self):
        self.driver.execute_script("window.scrollBy(0, 500);")

        pay_option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class = 'pmts-instrument-selector'])[1]")))
        pay_option.click()


        payment_clicks = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@data-cel-widget='checkout-secondary-continue-button-id']")))

        payment_clicks.click()

        payment_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@aria-labelledby = 'submitOrderButtonId-announce']")))

        payment_btn.click()

    def screenShot(self):
        self.driver.get_screenshot_as_file('screenshot8_.png')

        # add_card = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "(//a[text() = 'Add a new credit or debit card'])[1]")))

        # add_card.click()