from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.main_page import MainPage


def test_task_13(browser):
    page = BasePage(browser)
    main_page = MainPage(browser)
    cart_page = CartPage(browser)
    page.open("http://localhost/litecart/")
    main_page.add_product_to_cart()
    main_page.go_to_cart()
    cart_page.delete_from_cart()
