import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


@pytest.fixture
def browser(request):
    print("\nstart firefox browser for test..")
    browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()


def test_task_4(browser):
    def is_element_present(how, what):
        try:
            browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    browser.get("http://localhost/litecart/admin/")
    browser.find_element(By.XPATH, '//input[@name="username"]').send_keys('admin')
    browser.find_element(By.XPATH, '//input[@name="password"]').send_keys('admin')
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()
    rows = browser.find_elements(By.XPATH, '//ul[@id="box-apps-menu"]//li[@id="app-"]')
    for row in range(1, len(rows) + 1):
        col = browser.find_element(By.XPATH, f'//li[@id="app-"][{row}]')
        col.click()
        is_element_present(By.XPATH, '//h1')
        cells = browser.find_elements(By.XPATH, '//ul[@class="docs"]//li')
        if len(cells) > 0:
            for cell in range(1, len(cells) + 1):
                browser.find_element(By.XPATH, f'//ul[@class="docs"]//li[{cell}]').click()
                is_element_present(By.XPATH, '//h1')
