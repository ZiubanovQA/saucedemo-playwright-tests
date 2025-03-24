from playwright.sync_api import Page
from pages.base_page import BasePage

import time




class LoginPage(BasePage):
    
    def __init__(self, page: Page, test_name: str, url: str, open: bool=False):
        super().__init__(page, test_name, url)
        
        if open:
            self.open()
        
        self.username_input = self.page.locator('input[data-test="username"]')
        self.password_input = self.page.locator('input[data-test="password"]')
        self.login_button   = self.page.locator('input[data-test="login-button"]')
        self.error_message  = self.page.locator('h3[data-test="error"]')
        self.title_text     = self.page.locator('.title')
        
        
    def login(self, username: str, password: str) -> str | bool:
        self.username_input.fill(username)
        self.password_input.fill(password)

        self.login_button.click()
        
        if self.check_error():
            return self.error_text
        
        self.page.wait_for_url("**/inventory.html")
        
        if str(self.get_title()).lower() == 'products':
            return False
        return 'Login without redirect. Error not found'
        
        
    def check_error(self) -> bool:        
        if self.error_message.is_visible():
            self.error_text = self.error_message.inner_text()
            return True
        return False
    
    
    def get_title(self) -> str:
        return self.title_text.inner_text()