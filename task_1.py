import pytest
from selenium import webdriver


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
    browser.get("https://ya.ru/")
