import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def browser(request):
    print("\nstart firefox browser for test..")
    browser = webdriver.Firefox()

    # print("\nstart chrome browser for test..")
    # browser = webdriver.Chrome()

    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()


def is_not_element_present(browser, how, what, timeout=2):
    try:
        WebDriverWait(browser, timeout).until(EC.presence_of_element_located((how, what)))
    except TimeoutException:
        return True
    return False



def test_task_13(browser):
    def is_element_present(how, what):
        try:
            browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    browser.get("http://localhost/litecart/")
    for i in range(1, 4):
        browser.find_element(By.CSS_SELECTOR, f'li.product.column.shadow.hover-light:nth-child({i})').click()
        check = is_element_present(By.CSS_SELECTOR, 'select[name="options[Size]"]')
        if check:
            browser.find_element(By.CSS_SELECTOR, 'select[name="options[Size]"]').send_keys('Small')
        browser.find_element(By.CSS_SELECTOR, 'button[name="add_cart_product"]').click()
        WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'span.quantity'), f'{i}'))
        browser.find_element(By.CSS_SELECTOR, 'div#logotype-wrapper').click()
    browser.find_element(By.CSS_SELECTOR, 'div#cart a.link').click()
    shortcuts = browser.find_elements(By.CSS_SELECTOR, 'li.shortcut')
    for num in range(1, len(shortcuts) + 1):
        if is_element_present(By.CSS_SELECTOR, f'li.shortcut'):
            browser.find_element(By.CSS_SELECTOR, f'li.shortcut:nth-child(1)').click()
        item = browser.find_element(By.CSS_SELECTOR, f'li.item:nth-child(1)')
        duck_name = item.find_element(By.CSS_SELECTOR, 'strong').get_attribute("outerText")
        item.find_element(By.CSS_SELECTOR, 'button[name="remove_cart_item"]').click()
        is_not_element_present(browser, By.XPATH, f'//table[contains(@class, "dataTable")]//td[text()="{duck_name}"]')
