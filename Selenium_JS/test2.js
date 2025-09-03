const {Builder, By, Key, until} = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');

let options = new chrome.Options();
options.addArguments('start-maximized');

let driver = new Builder().forBrowser('chrome').setChromeOptions(options).build();

async function runTest() {
    await driver.get('https://www.youtube.com');
    await driver.wait(until.elementLocated(By.id('logo-icon')), 10000);
    //await driver.findElement(By.id('video-title')).click();
    await driver.findElement(By.name('search_query')).sendKeys('Selenium Tutorial', Key.RETURN);
    await driver.findElement(By.id('title')).click();
    expect(await driver.findElement(By.className('style-scope ytd-popup-container'))).Visible.toBe(true);
}

runTest().catch((error) => {
    console.error('Test failed:', error);
});