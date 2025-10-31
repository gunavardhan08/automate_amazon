from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="twotabsearchtextbox"]')))

    def search_product(self, product_name):
        self.search_box.send_keys(product_name)
        self.search_box.send_keys(Keys.ENTER)
        self.driver.execute_script("window.scrollBy(0, 250);")

    def select_product(self):
        product_selection = self.driver.find_elements(By.CSS_SELECTOR, "div.s-search-results img.s-image")
        found = False
        count = 0
        for item in range(len(product_selection)):
            count += 1
            if count == 1:        # In search results of phones, adding 1st phone to cart
                product_selection[item].click()
                found = True
                break

    def product_to_cart(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

        add_to_cart_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '(//*[@id="add-to-cart-button"])[2]')))

        add_to_cart_btn.click()

        proceed_to_cart = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'proceedToRetailCheckout')))

        proceed_to_cart.click()




