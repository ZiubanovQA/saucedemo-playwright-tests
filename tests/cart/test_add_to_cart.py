from pages.login_page import LoginPage
from pages.cart_page import CartPage

def test_remove_from_cart(browser):
    login_page = LoginPage(
        page=browser,
        test_name="test_login",
        url="https://www.saucedemo.com/"
    )
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    cart_page = CartPage(
        page=browser,
        test_name="test_remove_from_cart",
        url="https://www.saucedemo.com/inventory.html"
    )

    cart_page.add_to_cart()
    cart_page.remove_from_cart()

    cart_count = browser.locator(".shopping_cart_badge")
    assert cart_count.count() == 0, "Товар не удалился из корзины!"
