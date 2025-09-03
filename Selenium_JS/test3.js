const {Builder, By, Key, until} = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
//const { assert } = require('chai');


let driver;
before(async() => {
    driver = await new Builder().forBrowser('chrome').build();
}) 

it('Test Case 1', async() => {
    await driver.get('https://rahulshettyacademy.com/AutomationPractice/');
    await driver.findElement(By.name('radioButton')).click();
    // await driver.findElement(By.css('#radio-btn-example label:nth-child(3)')).click();
    await driver.findElement(By.id('dropdown-class-example')).click();
    await driver.findElement(By.css('option[value="option2"]')).click();
    await driver.findElement(By.id('displayed-text')).sendKeys('Test');
    await driver.findElement(By.id('hide-textbox')).click();
   print(await driver.findElement(By.id('show-textbox')),false);
});

// after(async () => {
//     await driver.quit();
// });