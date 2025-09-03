from playwright.sync_api import Locator, Page
import re
import pandas as pd

class HomePage:
    """Page Object for the Home Page of the application."""
    page_title_selector: str = ".brand.greenLogo"
    search_box_selector: str = ".search-keyword"
    searched_products_selector: str = "//div[@class='products']/div"

    def __init__(self, page):
        self.page = page
        self.page_title  = page.locator(self.page_title_selector)
        self.search_box = page.locator(self.search_box_selector)
        self.searched_products = page.locator(self.searched_products_selector)
        
    
    def get_text(self, elementName) -> Locator:
        """Get text from a required element on the page."""
        locator_value = ""
        match elementName:
            case "Title":
                locator_value = self.page_title
                ##assert self.page.get_by_role("heading", name="GREEN").is_visible(), "Title is not visible"

        return (locator_value).inner_text() 
    
    def search_items_and_assert_names(self, itemName: str):
        """Search for items on the home page and assert the names of resulted products contains searched word."""
        self.search_box.fill(itemName)
        self.page.wait_for_timeout(5000)
        #expect(self.page.locator(self.searched_products).filter(has_text=re.compile(r"nuts"))).to_be_visible()
        products_locator = self.page.locator(self.searched_products)      
        count = self.searched_products.count()
        for i in range(count):
            product_name = self.searched_products.nth(i).inner_text()
            print(f"Product found: {product_name}")
            assert itemName.lower() in product_name.lower(), f"Product '{product_name}' does not contain the searched term '{itemName}'"


    def psuedo_code(self):
        """This is a placeholder for pseudo code."""
        content = pd.read_csv("data.csv")
        content2 = pd.read_json("data.json")
        valeus = content2["key"].values

        open("file.txt", "w").write("Hello World")
        with open("file.txt", "r") as file:
            data = file.read()
            print(data)