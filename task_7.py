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


def test_task_4(browser):

    cards = []
    browser.get("http://localhost/litecart/en/")
    categories = browser.find_elements(By.CSS_SELECTOR, 'ul.products')
    for category in categories:
        cards += category.find_elements(By.CSS_SELECTOR, 'li.product')
    for card in cards:
        stickers = card.find_elements(By.CSS_SELECTOR, 'div.sticker')
        assert len(stickers) <= 1, "Карточка имеет 2 стикера"
