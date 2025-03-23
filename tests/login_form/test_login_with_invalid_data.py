import config as c

def test_login_with_invalid_data(browser):
    browser.goto("https://www.saucedemo.com/")

    browser.fill('input[data-test="username"]', 'invalid_username')
    browser.fill('input[data-test="password"]', 'invalid_password')

    browser.click('input[data-test="login-button"]')

    browser.screenshot(path=c.S_RESULT_PATH + "login_with_invalid_data.png")

    assert browser.url == "https://www.saucedemo.com/"

    error = browser.locator('h3[data-test="error"]').inner_text()
    assert "Username and password do not match" in error
