import {test, expect} from '@playwright/test';
import appsettings from './appsettings.json';

test.describe('Basic tests', () => {

    test('Provided url should land me on Instagram login page', async ({page}) => {
        await page.goto(appsettings.instagraSignInUrl);
        const pageTitle = await page.title();
        expect(pageTitle).toBe('Login • Instagram');
    })

    test('Provided url should land me on Youtube page and I will click on SignIn', async ({page, context}) => {
        await page.goto(appsettings.youtubeUrl);
        await page.waitForLoadState('networkidle');
        await page.click('text=Sign in');
        await page.waitForLoadState('networkidle');
        
       // Listen for the new page event
       const [newPage] = await Promise.all([
        context.waitForEvent('page'),
        await page.getByText('Learn more about using Guest mode').click()
        ]);

    // Wait for the new page to load
    await newPage.waitForLoadState('networkidle');
    expect(newPage.getByText('Open Guest mode')).toBeVisible();
    await newPage.waitForLoadState('networkidle');
    expect(newPage.locator('div[class="zippy-overflow"]')).toBeHidden();
    await newPage.locator('div[class="zippy-container zippy-last"]').click();
    expect(newPage.locator('div[class="zippy-overflow"]')).toBeVisible();
    });

    test('Redirect to Automation Practice page and try different operations', async({page})    =>{
        await page.goto(appsettings.automationPracticeUrl);
        expect(await page.title()).toBe('Practice Page');
        await page.locator('#dropdown-class-example').selectOption({label: 'Option3'});
        await page.getByPlaceholder('Enter Your Name').fill('Hello World');
        await page.locator('#alertbtn').click();
        expect(await page.locator('p[id="showalert"]').textContent()).toBe('Hello World');
    } )

    test('Redirect to Autamation practice page and check for table entries and sum', async({page}) =>{
        await page.goto(appsettings.automationPracticeUrl);
        const columnsCount = await page.locator('table[id="product"] thead th').count();
        console.log(columnsCount);
        for (let i = 1; i <= columnsCount; i++) {
            const text = await page.locator(`table[id="product"] thead th:nth-child(${i})`).textContent();
            expect(text).toContain(appsettings.tableColumnNames[i-1]);
        }
    })

})
