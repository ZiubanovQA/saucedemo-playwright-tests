from pages.login_page import LoginPage

def test_login_with_valid_data(browser):
    login_page = LoginPage(
        page=browser,
        test_name="test_login_with_valid_data",
        url="https://www.saucedemo.com/",
        open=True
    )

    result = login_page.login("standard_user", "secret_sauce")
    login_page.screenshot()
    
    assert result is False
