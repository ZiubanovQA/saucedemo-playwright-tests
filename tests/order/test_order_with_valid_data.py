import config as c

def test_order_with_valid_data(browser):

    browser.goto("https://www.saucedemo.com/")
    browser.fill('input[data-test="username"]', 'standard_user')
    browser.fill('input[data-test="password"]', 'secret_sauce')
    browser.click('input[data-test="login-button"]')

    browser.click('button[data-test="add-to-cart-sauce-labs-backpack"]')

    browser.click('a.shopping_cart_link')
    
    browser.click('button[data-test="checkout"]')

    browser.fill('input[data-test="firstName"]', 'Иван')
    browser.fill('input[data-test="lastName"]', 'Иванов')
    browser.fill('input[data-test="postalCode"]', '123456')
    browser.click('input[data-test="continue"]')

    browser.click('button[data-test="finish"]')

    browser.screenshot(path=c.SCREENSHOT_PATH + "order_with_valid_data.png")

    assert browser.locator('h2.complete-header').inner_text() == "Thank you for your order!"