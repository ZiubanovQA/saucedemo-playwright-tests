import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True)

    context = browser.new_context(
        viewport={"width": 1920, "height": 1080}
    )

    page = context.new_page()
    yield page

    context.close()
    browser.close()
