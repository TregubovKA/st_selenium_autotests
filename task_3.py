import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser(request):
    print("\nstart firefox browser for test..")
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.implicitly_wait(2)
    yield browser
    print("\nquit browser..")
    browser.quit()


def test_task_1(browser):
    browser.get("http://localhost/litecart/admin/")
    browser.find_element(By.XPATH, '//input[@name="username"]').send_keys('admin')
    browser.find_element(By.XPATH, '//input[@name="password"]').send_keys('admin')
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()
