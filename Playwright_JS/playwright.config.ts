import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  projects: [
    {
      name: 'firefox',
      use: { browserName: 'firefox' },
    },
    // {
    //   name: 'chromium',
    //   use: { browserName: 'chromium' },
    // },
    // {
    //   name: 'webkit',
    //   use: { browserName: 'webkit' },
    // },
  ],
  workers: 4,
  retries: 0,
  reporter: [['list'], ['html', { open: 'never' }]],
});
