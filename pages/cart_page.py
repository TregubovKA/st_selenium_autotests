from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    def delete_from_cart(self):
        shortcuts = self.browser.find_elements(By.CSS_SELECTOR, 'li.shortcut')
        for num in range(1, len(shortcuts) + 1):
            if self.is_element_present(By.CSS_SELECTOR, 'li.shortcut'):
                self.browser.find_element(By.CSS_SELECTOR, 'li.shortcut:nth-child(1)').click()
            item = self.browser.find_element(By.CSS_SELECTOR, 'li.item:nth-child(1)')
            duck_name = item.find_element(By.CSS_SELECTOR, 'strong').get_attribute("outerText")
            self.is_clickable(By.CSS_SELECTOR, 'li.item:nth-child(1) button[name="remove_cart_item"]')
            self.browser.find_element(By.CSS_SELECTOR, 'li.item:nth-child(1) button[name="remove_cart_item"]').click()
            self.is_not_element_present(By.XPATH, f'//table[contains(@class,"dataTable")]//td[text()="{duck_name}"]')
