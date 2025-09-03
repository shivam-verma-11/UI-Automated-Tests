import pytest
from playwright.sync_api import sync_playwright, Page, expect


@pytest.fixture(scope="function")
def redirected_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://rahulshettyacademy.com/AutomationPractice/")
        yield page
        page.close()
        browser.close()

#@pytest.parametrize("checkbox_id", ["checkBoxOption1", "checkBoxOption2", "checkBoxOption3"])
def test_trigger_alert_and_handle(redirected_page):
    """Should trigger an alert and handle it"""
    page = redirected_page
    dialog_message = ""

    def handle_dialog(dialog):
        nonlocal dialog_message
        dialog_message = dialog.message
        dialog.accept()

    page.on("dialog", handle_dialog)
    page.click('#alertbtn')
  
    assert (dialog_message) ==("Hello , share this practice page and share your knowledge")


def test_open_new_tab_and_verify(redirected_page):
    """Should open a new tab and verify the URL"""
    page = redirected_page
    
    with page.context.expect_page() as new_page_info:
        page.click('#openwindow')
    new_page = new_page_info.value
    new_page.wait_for_load_state("domcontentloaded")
    expect(new_page.locator("#about-part  h2")).to_be_visible()

def test_automation_pratice_website(redirected_page):
    """To try different operations on automation practice website """

    page = redirected_page
    with page.context.expect_page() as new_page_info:
        page.get_by_text('Open Window').click()
    new_page = new_page_info.value
    new_page.wait_for_load_state("domcontentloaded")
    new_page.close()

    with page.context.expect_page() as new_tab_info:
        page.get_by_text('Open Tab').click()
    new_tab = new_tab_info.value
    new_tab.wait_for_load_state("domcontentloaded")
    new_tab.close()

    iframe  = page.frame_locator('#courses-iframe')
    expect(iframe.get_by_text('Learn Earn & Shine')).to_be_visible()
    page.close()


def test_handle_alert(redirected_page):
    """To handle alert on automation practice website"""

    page = redirected_page
    dialog_message = ""

    def handle_dialog(dialog):
        nonlocal dialog_message
        dialog_message = dialog.message
        dialog.accept()

    # Register the dialog handler BEFORE triggering
    page.on("dialog", handle_dialog)
    
    page.evaluate("document.querySelector('#alertbtn').click()")
    
    # with page.expect_event("dialog") as dialog_info:                      |
    #     page.evaluate("document.querySelector('#alertbtn').click()")      |---> doesn't worked that way ( kept this comment to understand the difference)
    # dialog = dialog_info.value                                            |    

    assert dialog_message == "Hello , share this practice page and share your knowledge"

    
def test_land_on_MMT_and_verify_cities_in_from_list():
    """Should land on MMT and verify cities in 'From' list"""
    citiNames = ['Mumbai, India', 'New Delhi, India', 'Bangkok, Thailand', 'Bengaluru, India', 'Pune, India', 'Hyderabad, India',  'Kolkata, India', 'Chennai, India', 'Goa - Dabolim Airport, India', 'Dubai, United Arab Emirates']

    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless= False)                   #This test only words in headed mode due to bot protection in MMT
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.makemytrip.com/")
        
      
        page.wait_for_selector('.commonModal__close', state='visible')
        page.click('.commonModal__close')
        page.click('//input[@id="fromCity"]')
        
        page.wait_for_selector('(//li [@role="option"]//p)[1]', state='visible')
        options = page.locator('(//li [@role="option"]//p)').all_inner_texts()
        print("this is the required list", options)
        options = options[::2]
        print(options)
        for option in options:
            assert option in citiNames, f"City '{option}' not found in the expected list"
        page.close()
        browser.close()
