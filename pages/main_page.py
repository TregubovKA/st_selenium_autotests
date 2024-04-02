from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.product_page import ProductPage


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.product_page = ProductPage(self.browser)

    def open_product_page(self, i):
        self.browser.find_element(By.CSS_SELECTOR, f'li.product.column.shadow.hover-light:nth-child({i})').click()

    def add_product_to_cart(self, it=4):
        for i in range(1, it):
            self.open_product_page(i)
            self.product_page.check_selector_presence()
            self.product_page.add_product_to_card(i)
            self.product_page.go_to_main_page()

    def go_to_cart(self):
        self.browser.find_element(By.CSS_SELECTOR, 'div#cart a.link').click()
