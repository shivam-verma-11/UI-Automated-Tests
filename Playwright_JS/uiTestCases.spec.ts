import {test, expect} from '@playwright/test';
import defineConfig from './playwright.config.ts';
import appsettings from './appsettings.json';

//test.describe.configure({ mode: 'parallel' });

test.describe('Basic tests', () => {

    test('Provided url should land me on Instagram login page and then I open new page in new context', async ({page, browser}) => {
        // // var context = playwright.chromium.launch()
        // // var browser = (await context).newContext();
        // // var page = (await browser).newPage();
        await page.goto(appsettings.instagraSignInUrl);
        const pageTitle = await page.title();
        expect(pageTitle).toBe('Login • Instagram');
        const context = await browser.newContext();
        const newPage = await context.newPage();
    })

    test('Provided url should land me on Youtube page and I will click on SignIn', async ({page, context}) => {
        await page.goto(appsettings.youtubeUrl);
        await page.waitForLoadState('networkidle');
        await page.click('text=Sign in');
        await page.waitForLoadState('networkidle');
        
       // Listen for the new page event
       const [newPage] = await Promise.all([
        context.waitForEvent('page'),
        page.getByText('Learn more about using Guest mode').click()
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

    test('Redirect to Autamation practice page and handle alert', async({page}) =>{
        await page.goto(appsettings.automationPracticeUrl);

        // Set up the dialog handler BEFORE the click
        page.once('dialog', async (dialog) => {
        expect(dialog.message()).toBe('Hello , share this practice page and share your knowledge');
        await dialog.accept();
        });
        await page.locator('#alertbtn').waitFor({ state: 'visible' });
        await page.locator('#alertbtn').click();
        //await page.evaluate("document.querySelector('#alertbtn').click()");
    })

    test('Check download on chrome only', async ({page, browserName}) => {
        test.skip(browserName !== 'chromium', 'This test is only for Chrome');
        await page.goto('appsettings.downloadUrl');
        try{
            const downloadPromise = page.waitForEvent('download');
            await page.click('text=Download');
            const download = await downloadPromise;
            expect(download.suggestedFilename()).toBe('example.txt');
            download.saveAs('example.txt');
        }
        catch (error) {
            console.error('Download failed due to:', error);
        }
        
    })

    test.only('Land on MMT page and check list of cities', async ({page}) => {
        const cityNames = ['Mumbai, India', 'New Delhi, India', 'Bangkok, Thailand', 'Bengaluru, India', 'Pune, India', 'Hyderabad, India',  'Kolkata, India', 'Chennai, India', 'Goa - Dabolim Airport, India', 'Dubai, United Arab Emirates'];
        await page.goto('https://www.makemytrip.com/');
        await page.locator('.commonModal__close').waitFor({ state: 'visible' });
        await page.locator('.commonModal__close').click();
        await page.locator('//input[@id="fromCity"]').click()
        const value = (await  page.locator('(//li [@role="option"]//p)[1]').innerText());
        expect(value).toBe('Mumbai, India');

        const options = await page.locator('//li[@role="option"]//p').allInnerTexts();
        let cityNamesOptions: Array<string> = [];
        for(let i=0; i< options.length/2; i++) {
            cityNamesOptions.push(options[(2*i)]);
        }
        expect(cityNamesOptions).toEqual(cityNames);
    })
});