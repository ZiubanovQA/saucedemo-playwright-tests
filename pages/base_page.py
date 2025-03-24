from playwright.sync_api import Page

import config




class BasePage:
    
    def __init__(self, page: Page, test_name: str, url: str):
        self.page      = page
        self.test_name = test_name
        self.url       = url
        
        
    def screenshot(self) -> None:
        self.page.screenshot(path=f"{config.SCREENSHOT_PATH}{self.test_name}.png")
        
        
    def open(self) -> None:
        self.page.goto(self.url)
        