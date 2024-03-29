import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart Firefox browser for test..")
    browser = webdriver.Firefox()
    browser.maximize_window()
    # browser.implicitly_wait(2)
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()
