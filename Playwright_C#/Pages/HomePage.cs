using Microsoft.Playwright;
using System.Threading.Tasks;

namespace GreenCartTests.Pages
{
    public class HomePage
    {
        private readonly IPage page;

        public HomePage(IPage pages)
        {
            page = pages;
        }

        public async Task RedirectToHomePage(string url)
        {
            await page.GotoAsync(url);
            await page.SetViewportSizeAsync(1280, 720);
        }

        public async Task<string> GetPageTitle()
        {
            return await page.TitleAsync();
        }
    }
}
