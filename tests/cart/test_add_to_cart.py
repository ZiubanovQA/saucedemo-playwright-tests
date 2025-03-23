import config as c

def test_add_item_to_cart(browser):
    browser.goto("https://www.saucedemo.com/")
    browser.fill('input[data-test="username"]', 'standard_user')
    browser.fill('input[data-test="password"]', 'secret_sauce')
    browser.click('input[data-test="login-button"]')

    browser.click('button[data-test="add-to-cart-sauce-labs-backpack"]')
    browser.click('a.shopping_cart_link')

    browser.screenshot(path=c.S_RESULT_PATH + "add_to_cart.png")
    
    assert browser.locator('.cart_item').count() == 1
    assert browser.locator('.inventory_item_name').inner_text() == "Sauce Labs Backpack"
