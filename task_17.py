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
    for l in browser.get_log("browser"):
        print(l)
    print("\nquit browser..")
    browser.quit()


def test_task_14(browser):
    browser.get('http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1')
    browser.find_element(By.XPATH, '//input[@name="username"]').send_keys('admin')
    browser.find_element(By.XPATH, '//input[@name="password"]').send_keys('admin')
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()
    browser.find_element(By.XPATH, '//a[text()="Subcategory"]').click()
    rows = browser.find_elements(By.CSS_SELECTOR, 'table.dataTable tr.row')
    for i in range(5, len(rows) + 2):
        row = browser.find_element(By.CSS_SELECTOR, f'table.dataTable tr.row:nth-child({i})')
        links = row.find_elements(By.CSS_SELECTOR, 'a')
        for a in range(1, len(links) + 1):
            link = browser.find_element(By.CSS_SELECTOR, f'table.dataTable tr.row:nth-child({i}) a:nth-child({a})')
            if link.get_property("title") != "Edit":
                link.click()
                browser.find_element(By.CSS_SELECTOR, 'button[name="cancel"]').click()
