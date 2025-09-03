import pytest
from playwright.sync_api import sync_playwright, Page, expect
from PageObjects.HomePage import HomePage


@pytest.fixture(scope="function")
def browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")
        home_page = HomePage(page)
        yield page, home_page
        page.close()
        context.close()
        browser.close()

def test_redirect_to_greenkart_and_verify(browser_page):
    """Should redirect to google.com and verify the URL"""
    home_page = browser_page
    actual_title = home_page.get_text("Title")
    assert actual_title == "GREENKART", f"Expected 'GREENKART', but got '{actual_title}'"
    

def test_search_for_cucumber(browser_page):
    """Should search for cucumber and verify the search results"""
    home_page = browser_page
    home_page.search_items_and_assert_names("nuts")
    

def test_dummy(page: Page):
    """Dummy test to ensure the page is working."""
    page.goto("https://www.google.com/")
    page.wait_for_load_state("domcontentloaded")
    assert "Google" in page.title(), "Google title not found"

    









    
    