import os,sys
import time

import pytest
from selenium.common import WebDriverException

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.product import ProductPage
from pages.login1 import LoginPage
from pages.check_out import Payment_Page


def test_product_search():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://www.amazon.in")

        product_page = ProductPage(driver)

        product_page.search_product("oneplus 13r")

        product_page.select_product()

        product_page.product_to_cart()

        login_page = LoginPage(driver)
        login_page.login_user("email80@gmail.com")  # give email id
        login_page.login_password("password8")      #give password

        payment_page = Payment_Page(driver)
        payment_page.payment_check()
        payment_page.screenShot()

        if "503 Service Unavailable" in driver.page_source:
            print("Amazon returned a 503 Service Unavailable error.")
            pytest.skip("503 error encountered during test run.")
        else:
            print("Test ran successfully")


    except WebDriverException as e:
        if "503" in str(e):
            print("Caught WebDriverException with 503 error:", e)
            pytest.skip("503 error encountered in WebDriver.")
        else:
            raise

    finally:
        driver.quit()







