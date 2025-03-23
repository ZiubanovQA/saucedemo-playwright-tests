import config as c

def test_login_with_valid_data(browser):
    browser.goto("https://www.saucedemo.com/")

    browser.fill('input[data-test="username"]', 'standard_user')
    browser.fill('input[data-test="password"]', 'secret_sauce')

    browser.click('input[data-test="login-button"]')
    
    browser.screenshot(path=c.S_RESULT_PATH + "login_with_valid_data.png")
    
    assert browser.url == "https://www.saucedemo.com/inventory.html"
    assert browser.locator('.title').inner_text() == "Products"