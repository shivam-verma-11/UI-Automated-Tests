// Import necessary modules
const { Builder, By, Key, until } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');

// Create a function to run the test
async function runTest() {
    // Set up the Chrome options (Optional)
    let options = new chrome.Options();
    options.addArguments('start-maximized'); // Open browser maximized

    // Initialize the WebDriver instance with Chrome
    let driver = await new Builder().forBrowser('chrome').setChromeOptions(options).build();

    try {
        // Navigate to a website (e.g., Google)
        await driver.get('https://www.google.com');

        // Wait until the page is loaded (Check for the Google search box)
        await driver.wait(until.elementLocated(By.name('q')), 10000);

        // Find the search input box using the name attribute and send keys
        let searchBox = await driver.findElement(By.name('q'));

        await searchBox.sendKeys('Selenium WebDriver with JavaScript', Key.RETURN);  // Press ENTER after typing

        // Wait for the search results to load
        await driver.wait(until.elementLocated(By.id('search')), 10000);

        // Find the first link in the search results and click it
        let firstLink = await driver.findElement(By.css('h3')).click();

        // Verify the title of the page after clicking
        let title = await driver.getTitle();
        console.log('Page Title: ' + title);

    } finally {
        // Close the browser after the test
        await driver.quit();
    }
}

// Run the test
runTest().catch((error) => {
    console.error('Test failed:', error);
});
