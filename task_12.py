from datetime import datetime, timedelta
import os.path
import random

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By



@pytest.fixture
def browser(request):
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome()

    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()


def rand_nums_generator():
    str1 = '1234567890'
    ls = list(str1)
    random.shuffle(ls)
    nums = ''.join([random.choice(ls) for x in range(5)])
    return nums


def rand_words_generator():
    str1 = 'qwertyuiopasdfghjklzxcvbnm'
    ls = list(str1)
    random.shuffle(ls)
    name = ''.join([random.choice(ls) for x in range(6)])
    return name


def is_element_present(browser, how, what):
    try:
        browser.find_element(how, what)
    except NoSuchElementException:
        return False
    return True


def test_task_12(browser):
    browser.get("http://localhost/litecart/admin/")
    browser.find_element(By.XPATH, '//input[@name="username"]').send_keys('admin')
    browser.find_element(By.XPATH, '//input[@name="password"]').send_keys('admin')
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()
    browser.find_element(By.XPATH, '//span[text()="Catalog"]').click()
    browser.find_element(By.XPATH, '//a[text()=" Add New Product"]').click()
    selector_status = browser.find_element(By.XPATH, '//label[text()=" Enabled"]/input')
    if not selector_status.get_property('checked'):
        selector_status.click()
    product_name = rand_words_generator()
    browser.find_element(By.CSS_SELECTOR, 'input[name="name[en]"]').send_keys(product_name)
    product_code = rand_nums_generator()
    browser.find_element(By.CSS_SELECTOR, 'input[name="code"]').send_keys(product_code)
    browser.find_element(By.CSS_SELECTOR, 'input[data-name="Rubber Ducks"]').click()
    browser.find_element(By.CSS_SELECTOR, 'input[data-name="Subcategory"]').click()
    browser.find_element(By.CSS_SELECTOR, 'select[name="default_category_id"]').send_keys('Subcategory')
    quantity = browser.find_element(By.CSS_SELECTOR, 'input[name="quantity"]')
    quantity.clear()
    quantity.send_keys(5)
    browser.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(os.path.abspath('test_pic.png'))
    browser.find_element(By.CSS_SELECTOR, 'input[name="date_valid_from"]')\
        .send_keys(datetime.now().strftime('%d.%m.%Y'))
    week_delta = timedelta(weeks=1)
    browser.find_element(By.CSS_SELECTOR, 'input[name="date_valid_to"]').send_keys((datetime.now()+week_delta)
                                                                                   .strftime('%d.%m.%Y'))

    browser.find_element(By.XPATH, '//a[text()="Information"]').click()
    browser.find_element(By.CSS_SELECTOR, 'select[name="manufacturer_id"]').send_keys('ACME Corp')

    browser.find_element(By.XPATH, '//a[text()="Prices"]').click()
    browser.find_element(By.CSS_SELECTOR, 'input[name="purchase_price"]').send_keys(15)
    browser.find_element(By.CSS_SELECTOR, 'select[name="purchase_price_currency_code"').send_keys("US Dollars")
    browser.find_element(By.CSS_SELECTOR, 'input[name="gross_prices[USD]"]').send_keys(10)
    browser.find_element(By.CSS_SELECTOR, 'button[name="save"]').click()
    assert is_element_present(browser, By.XPATH, f'//a[text()="{product_name}"]')
