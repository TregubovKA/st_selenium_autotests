import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait


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


def find_new_window_and_switch_to(browser, main_window, old_windows):
    for window in old_windows:
        if main_window != window:
            browser.switch_to.window(window)


def test_task_14(browser):
    browser.get('http://localhost/litecart/admin/?app=countries&doc=countries')
    browser.find_element(By.XPATH, '//input[@name="username"]').send_keys('admin')
    browser.find_element(By.XPATH, '//input[@name="password"]').send_keys('admin')
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()
    browser.find_element(By.XPATH, '//a[text()="Afghanistan"]').click()
    external_links = browser.find_elements(By.CSS_SELECTOR, 'i.fa-external-link')
    for link in external_links:
        main_window = browser.current_window_handle
        link.click()
        old_windows = browser.window_handles
        wait(browser, 5).until(EC.number_of_windows_to_be(2))
        find_new_window_and_switch_to(browser, main_window, old_windows)
        browser.close()
        browser.switch_to.window(main_window)
