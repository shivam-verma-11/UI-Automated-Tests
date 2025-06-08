using GreenCartTests.Pages;
using Microsoft.Playwright;

namespace GreenCartTests
{
    public class Tests
    {
        IPage page;
        IPlaywright playwright;
        HomePage homePage;

        [SetUp]
        public async Task Setup()
        {
            await BrowserContextSetup();
            homePage = new HomePage(page);
        }

        private async Task BrowserContextSetup()
        {
            playwright = await Playwright.CreateAsync();
            var browser = await playwright.Chromium.LaunchAsync(new BrowserTypeLaunchOptions { Headless = false });
            var context = await browser.NewContextAsync();
            page = await context.NewPageAsync();
        }

        [Test]
        public async Task WhenIRedirectToUrlOfGreenCart_ThenILandOnGreenCartHomePage()
        {
            await homePage.RedirectToHomePage("https://rahulshettyacademy.com/seleniumPractise/#/");
            var pageTitle = await homePage.GetPageTitle();
            Assert.That(pageTitle, Does.Contain("GreenKart"), "Expected Title to contain 'GreenCart' but it is present in the title");
        }
    }
}