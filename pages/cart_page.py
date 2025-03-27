from playwright.sync_api import Page
from pages.base_page import BasePage





class CartPage(BasePage):
    
    def __init__(self, page: Page, test_name: str, url: str, should_open: bool = True):
        super().__init__(page, test_name, url)
        
        if should_open:
            self.open()
        

        self.add_to_cart_button = self.page.locator('button[data-test="add-to-cart-sauce-labs-backpack"]')
        self.remove_button = self.page.locator('button[data-test="remove-sauce-labs-backpack"]')
        self.shopping_cart = self.page.locator('a.shopping_cart_link')
    
    def add_to_cart(self) -> None:
        self.add_to_cart_button.wait_for(state="visible")
        self.add_to_cart_button.click()
        self.shopping_cart.wait_for(state="visible")
        self.shopping_cart.click()
    
    def remove_from_cart(self) -> None:
        self.remove_button.wait_for(state="visible")
        self.remove_button.click()
