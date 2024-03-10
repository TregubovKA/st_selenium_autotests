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


def test_task_8(browser):
    countries = []
    browser.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    browser.find_element(By.XPATH, '//input[@name="username"]').send_keys('admin')
    browser.find_element(By.XPATH, '//input[@name="password"]').send_keys('admin')
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()
    rows = browser.find_elements(By.CSS_SELECTOR, 'tr.row')
    for a in range(1, len(rows)):
        country = browser.find_element(By.XPATH, f'//tr[@class="row"][{a}]//td[5]').get_attribute('innerText')
        countries.append(country)
        cnt_geozones = browser.find_element(By.XPATH, f'//tr[@class="row"][{a}]//td[6]').get_attribute('innerText')
        if int(cnt_geozones) > 0:
            browser.find_element(By.CSS_SELECTOR, 'tr.row td:nth-child(5) a').click()
            geozones = browser.find_elements(By.CSS_SELECTOR, 'table#table-zones tr')
            geozones_list = []
            for i in range(2, len(geozones) - 1):
                geozones_table_els = browser.find_element(By.XPATH, f'//table[@id="table-zones"]//tr[{i}]')
                geozones_list.append(geozones_table_els.find_element(By.CSS_SELECTOR, 'td:nth-child(3)')
                                     .get_attribute('innerText'))
            form_geozones_list = sorted(geozones_list)
            assert form_geozones_list == geozones_list, f"Геозоны {country} расположены не в алфавитном порядке"
            browser.find_element(By.XPATH, '//button[@name="cancel"]').click()
    form_countries = sorted(countries)
    assert countries == form_countries, "Страны расположены не в алфавитоном порядке"
