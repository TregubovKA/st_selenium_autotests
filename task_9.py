import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser(request):
    print("\nstart firefox browser for test..")
    browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()


def test_task_9(browser):
    browser.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    browser.find_element(By.XPATH, '//input[@name="username"]').send_keys('admin')
    browser.find_element(By.XPATH, '//input[@name="password"]').send_keys('admin')
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()
    rows = browser.find_elements(By.CSS_SELECTOR, 'tr.row')
    for a in range(1, len(rows) + 1):
        browser.find_element(By.XPATH, f'//tr[@class="row"][{a}]/td[3]/a').click()
        zones_selectors = browser.find_elements(By.XPATH, '//select[contains(@name, "[zone_code]")]')
        zones_list = []
        for zone_sel in zones_selectors:
            zones_list.append(zone_sel.find_element(By.CSS_SELECTOR, 'option[selected="selected"]')
                              .get_attribute('innerText'))
        sorted_zones_list = sorted(zones_list)
        assert sorted_zones_list == zones_list, "Зоны расположены не в алфавитном порядке"
        browser.find_element(By.XPATH, '//button[@name="cancel"]').click()




