from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_page import BasePage


class ProductPage(BasePage):

    def check_selector_presence(self):
        check = self.is_element_present(By.CSS_SELECTOR, 'select[name="options[Size]"]')
        if check:
            self.browser.find_element(By.CSS_SELECTOR, 'select[name="options[Size]"]').send_keys('Small')

    def add_product_to_card(self, i):
        self.browser.find_element(By.CSS_SELECTOR, 'button[name="add_cart_product"]').click()
        WebDriverWait(self.browser, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'span.quantity'),
                                                                              f'{i}'))

    def go_to_main_page(self):
        self.browser.find_element(By.CSS_SELECTOR, 'div#logotype-wrapper').click()
