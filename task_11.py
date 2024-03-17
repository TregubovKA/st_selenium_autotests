import random
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser(request):
    # print("\nstart firefox browser for test..")
    # browser = webdriver.Firefox()

    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome()

    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()


def rand_pass_generator():
    str1 = '123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str1 + str2 + str3
    ls = list(str4)
    random.shuffle(ls)
    pswrd = ''.join([random.choice(ls) for x in range(8)])
    return pswrd


def rand_mail_generator():
    str1 = 'qwertyuiopasdfghjklzxcvbnm'
    ls = list(str1)
    random.shuffle(ls)
    email = ''.join([random.choice(ls) for x in range(8)])
    return email


def rand_number_generator():
    nums = '12345678'
    ls = list(nums)
    random.shuffle(ls)
    number = ''.join([random.choice(ls) for x in range(10)])
    return number


def test_task_11(browser):
    browser.get("http://localhost/litecart/en/create_account")
    browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]').send_keys("Kirill")
    browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]').send_keys("Test")
    browser.find_element(By.CSS_SELECTOR, 'input[name="address1"]').send_keys("Kukueva st.")
    browser.find_element(By.CSS_SELECTOR, 'input[name="postcode"]').send_keys("24800")
    browser.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys("Kaluga")
    browser.find_element(By.CSS_SELECTOR, 'span.select2').click()
    browser.find_element(By.XPATH, '//li[text()="United States"]').click()
    email = rand_mail_generator() + '@gmail.com'
    browser.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys(email)
    browser.find_element(By.CSS_SELECTOR, 'input[type="tel"]').send_keys('+1' + rand_number_generator())
    pswrd_user = rand_pass_generator()
    browser.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(pswrd_user)
    browser.find_element(By.CSS_SELECTOR, 'input[name="confirmed_password"]').send_keys(pswrd_user)
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    browser.find_element(By.XPATH, '//a[text()="Logout"]').click()
    browser.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys(email)
    browser.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(pswrd_user)
    browser.find_element(By.CSS_SELECTOR, 'button[name="login"]').click()
    browser.find_element(By.XPATH, '//a[text()="Logout"]').click()
