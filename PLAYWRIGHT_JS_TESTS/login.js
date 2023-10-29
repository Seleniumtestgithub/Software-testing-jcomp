// login.js
const { expect } = require('@playwright/test');

async function login(page) {
        await page.goto('https://github.com/login');

        await page.getByLabel('Username or email address').click();
        await page.getByLabel('Username or email address').fill('Seleniumtestgithub');
        await page.getByLabel('Password').click();
        await page.getByLabel('Password').fill('throwawaygithub');
        await page.getByRole('button', { name: 'Sign in', exact: true }).click({timeout: 10000});

        await expect(page.getByLabel('Open user account menu')).toBeVisible();
    }
    
module.exports = { login };

  