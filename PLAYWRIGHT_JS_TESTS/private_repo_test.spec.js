const { test, expect } = require('@playwright/test');
const winston = require('winston');
const axios = require('axios');
const { login } = require('./login');
const token = "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";
const username = "st-jcomp-throwaway";
const password = "throwawaygithub";
const repoName = "github-automation-p980";  
  
//Create a logger that writes to a file
const logger = winston.createLogger({
        level: 'info',
        format: winston.format.combine(
                winston.format.timestamp(),
                winston.format.printf(info => `${info.timestamp} ${info.level}: ${info.message} [${info.test}] (${require('path').join(__dirname, 'tests')}`)),
        defaultMeta: { service: 'user-service' },
        transports: [
                new winston.transports.Console(),
                new winston.transports.File({ filename: 'combined.log' }),
        ],
});

test.use({ 
    reporter: 'list', 
    retries: 5, // Allow up to 5 retries for each test
  });
  

test('Make repository private', async ({ page }) => {
        await login(page);
        await page.pause();
        try {
        // Navigate to the repository's settings page
        await page.goto(`https://github.com/${username}/${repoName}/settings`);
        await page.getByRole('button', { name: 'Change visibility' }).click();
        await page.pause();
        await expect(page.getByRole('menuitem', { name: 'Change to private' })).toBeVisible();
        await page.getByRole('menuitem', { name: 'Change to private' }).click();
        await page.getByRole('button', { name: 'I want to make this repository private' }).click();
        await page.getByRole('button', { name: 'I have read and understand these effects' }).click();
        await page.getByRole('button', { name: 'Make this repository private' }).click();
        logger.info('Private repo test passed', { test: 'Private repo test' });
    } catch (error) {
      // Log the test result
      logger.error('Private repo test failed', { test: 'Private repo test', error });
  
      // Rethrow the error so the test fails
      throw error;
    }
});

// test('Make repository public', async ({ page }) => {
//     await login(page);
//     await page.pause();
//     try {
//     // Navigate to the repository's settings page
//     await page.goto(`https://github.com/${username}/${repoName}/settings`);
//     await page.getByRole('button', { name: 'Change visibility' }).click();
//     await page.pause();
//     await expect(page.getByRole('menuitem', { name: 'Change to public' })).toBeVisible();
//     await page.getByRole('menuitem', { name: 'Change to public' }).click();
//     await page.getByRole('button', { name: 'I want to make this repository public' }).click();
//     await page.getByRole('button', { name: 'I have read and understand these effects' }).click();
//     await page.getByRole('button', { name: 'Make this repository public' }).click();
//     logger.info('Public repo test passed', { test: 'Public repo test' });
//     } catch (error) {
//       // Log the test result
//       logger.error('Public repo test failed', { test: 'Public repo test', error });
  
//       // Rethrow the error so the test fails
//       throw error;
//     }
// });
