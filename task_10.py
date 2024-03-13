import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser(request):

    print("\nstart firefox browser for test..")
    browser = webdriver.Firefox()

    # print("\nstart chrome browser for test..")
    # browser = webdriver.Chrome()

    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()


def get_color_code(color_code_var):
    standard_color = color_code_var.split('(')
    standard_code = standard_color[1][0:len(standard_color[1])-1].split(", ")
    return standard_code


def test_task_10(browser):
    browser.get("http://localhost/litecart/")
    product_card = browser.find_element(By.CSS_SELECTOR, 'div#box-campaigns li')
    main_page_name = product_card.find_element(By.CSS_SELECTOR, 'div.name').get_attribute('innerText')
    main_page_price = product_card.find_element(By.CSS_SELECTOR, 's.regular-price')
    main_page_price_value = main_page_price.get_attribute('innerText')
    main_page_price_font_size = float(main_page_price.value_of_css_property('font-size').split('px')[0])
    main_page_price_crossed = main_page_price.value_of_css_property('text-decoration').split(" ")[0]
    assert main_page_price_crossed == 'line-through', 'Линия у базовой цены не зачеркнута'
    main_page_price_color = main_page_price.value_of_css_property('color')
    price_color_code = get_color_code(main_page_price_color)
    assert price_color_code[0] == price_color_code[1] == price_color_code[2], 'Цвет не серый'

    main_page_disc_price = product_card.find_element(By.CSS_SELECTOR, 'strong.campaign-price')
    main_page_disc_price_value = main_page_disc_price.get_attribute('innerText')
    main_page_disc_price_font_size = float(main_page_disc_price.value_of_css_property('font-size').split('px')[0])
    assert main_page_disc_price_font_size > main_page_price_font_size, "Скидочная цена не больше обычной по размеру"
    main_page_disc_price_color = main_page_disc_price.value_of_css_property('color')
    disc_price_color_code = get_color_code(main_page_disc_price_color)
    assert disc_price_color_code[1] == disc_price_color_code[2] == '0', 'Цвет не "красный'
    disc_price_width = int(main_page_disc_price.value_of_css_property('font-weight'))
    assert disc_price_width >= 700, "Скидочная цена отмечена нежирным цветом"

    product_card.click()
    product_page_name = browser.find_element(By.CSS_SELECTOR, 'h1.title').get_attribute('innerText')
    assert main_page_name == product_page_name, "Имена на разных страницах отличаются"
    product_page_price = browser.find_element(By.CSS_SELECTOR, 's.regular-price')
    product_page_price_value = product_page_price.get_attribute('innerText')
    assert main_page_price_value == product_page_price_value, "Базовая цена на разных страницах отличается"
    product_page_price_font_size = float(product_page_price.value_of_css_property('font-size').split('px')[0])
    product_page_price_crossed = product_page_price.value_of_css_property('text-decoration').split(" ")[0]
    assert product_page_price_crossed == 'line-through', 'Линия у базовой цены не зачеркнута'
    product_page_price_color = product_page_price.value_of_css_property('color')
    product_page_price_color_code = get_color_code(product_page_price_color)
    assert product_page_price_color_code[0] == product_page_price_color_code[1] == product_page_price_color_code[2], \
        'Цвет не серый'

    product_page_disc_price = browser.find_element(By.CSS_SELECTOR, 'strong.campaign-price')
    product_page_disc_price_value = product_page_disc_price.get_attribute('innerText')
    assert main_page_disc_price_value == product_page_disc_price_value, "Скидочная цена на разных страницах отличается"
    product_page_disc_price_font_size = float(product_page_disc_price.value_of_css_property('font-size').split('px')[0])
    assert product_page_disc_price_font_size > product_page_price_font_size, \
        "Скидочная цена не больше обычной по размеру"
    product_page_disc_price_color = product_page_disc_price.value_of_css_property('color')
    product_page_disc_price_color_code = get_color_code(product_page_disc_price_color)
    assert product_page_disc_price_color_code[1] == product_page_disc_price_color_code[2] == '0', 'Цвет не "красный'
    product_page_disc_price_width = int(product_page_disc_price.value_of_css_property('font-weight'))
    assert product_page_disc_price_width >= 700, "Скидочная цена отмечена нежирным цветом"
