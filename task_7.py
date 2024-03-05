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
    def is_element_present_in_card(how, what):
        try:
            card.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
    cards = []
    browser.get("http://localhost/litecart/en/")
    categories = browser.find_elements(By.CSS_SELECTOR, 'ul.listing-wrapper.products')
    for category in categories:
        cards += category.find_elements(By.CSS_SELECTOR, 'li.product.column.shadow.hover-light')
    for card in cards:
        sticker_sale = is_element_present_in_card(By.CSS_SELECTOR, 'div.sticker.sale')
        sticker_new = is_element_present_in_card(By.CSS_SELECTOR, 'div.sticker.new')

        assert sticker_new != sticker_sale, "Карточка имеет 2 стикера"
