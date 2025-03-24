from pages.login_page import LoginPage

def test_login_with_invalid_data(browser):
    login_page = LoginPage(
        page=browser,
        test_name="test_login_with_invalid_data",
        url="https://www.saucedemo.com/"
    )
    
    login_page.open()
    login_result = login_page.login("inv@l1d", " ")
    
    print("\n" + login_result)
    
    assert login_result is not False
