const { test, expect } = require('@playwright/test');
const winston = require('winston');

// Create a logger that writes to a file
const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.json()
  ),
  transports: [
    new winston.transports.File({ filename: 'test.log' })
  ]
});

test('Login demo test 1', async ({ page }) => {
  try {
    await page.goto('https://github.com/login');

    await page.getByLabel('Username or email address').click();
    await page.getByLabel('Username or email address').fill('Seleniumtestgithub');
    await page.getByLabel('Password').click();
    await page.getByLabel('Password').fill('throwawaygithub');
    await page.getByRole('button', { name: 'Sign in', exact: true }).click({timeout: 10000});

    await expect(page.getByLabel('Open user account menu')).toBeVisible();

    // Log the test result
    logger.info('Login demo test 1 passed', { test: 'Login demo test 1' });
  } catch (error) {
    // Log the test result
    logger.error('Login demo test 1 failed', { test: 'Login demo test 1', error });

    // Rethrow the error so the test fails
    throw error;
  }
});

test('Login demo test 2', async ({ page }) => {
  try {
    await page.goto('https://github.com/login');

    await page.getByLabel('Username or email address').click();
    await page.getByLabel('Username or email address').fill('Seleniumtestgithub2');
    await page.getByLabel('Password').click();
    await page.getByLabel('Password').fill('throwawaygithub');
    await page.getByRole('button', { name: 'Sign in', exact: true }).click({timeout: 10000});

    await expect(page.getByLabel('Open user account menu')).toBeVisible();

    // Log the test result
    logger.info('Login demo test 2 passed', { test: 'Login demo test 2' });
  } catch (error) {
    // Log the test result
    logger.error('Login demo test 2 failed', { test: 'Login demo test 2', error });

    // Rethrow the error so the test fails
    throw error;
  }
});

test('Login demo test 3', async ({ page }) => {
    try {
      await page.goto('https://github.com/login');
  
      await page.getByLabel('Username or email address').click();
      await page.getByLabel('Username or email address').fill('Seleniumtestgithub123');
      await page.getByLabel('Password').click();
      await page.getByLabel('Password').fill('throwawaygithub');
      await page.getByRole('button', { name: 'Sign in', exact: true }).click({timeout: 10000});

      await expect(page.getByLabel('Open user account menu')).toBeVisible();

      // Log the test result
      logger.info('Login demo test 3 passed', { test: 'Login demo test 3' });
    } catch (error) {
      // Log the test result
      logger.error('Login demo test 3 failed', { test: 'Login demo test 3', error });
  
      // Rethrow the error so the test fails
      throw error;
    }
  });

test('Login demo test 4', async ({ page }) => {
    try {
      await page.goto('https://github.com/login');
  
      await page.getByLabel('Username or email address').click();
      await page.getByLabel('Username or email address').fill('Seleniumtestgithub');
      await page.getByLabel('Password').click();
      await page.getByLabel('Password').fill('throwawaygithub123');
      await page.getByRole('button', { name: 'Sign in', exact: true }).click({timeout: 10000});

      await expect(page.getByLabel('Open user account menu')).toBeVisible();

      // Log the test result
      logger.info('Login demo test 4 passed', { test: 'Login demo test 4' });
    } catch (error) {
      // Log the test result
      logger.error('Login demo test 4 failed', { test: 'Login demo test 4', error });
  
      // Rethrow the error so the test fails
      throw error;
    }
  });

test('Login demo test 5', async ({ page }) => {
    try {
      await page.goto('https://github.com/login');
  
      await page.getByLabel('Username or email address').click();
      await page.getByLabel('Username or email address').fill('Seleniumtestgithub123');
      await page.getByLabel('Password').click();
      await page.getByLabel('Password').fill('throwawaygithub123');
      await page.getByRole('button', { name: 'Sign in', exact: true }).click({timeout: 10000});

      await expect(page.getByLabel('Open user account menu')).toBeVisible();
      
      // Log the test result
      logger.info('Login demo test 5 passed', { test: 'Login demo test 5' });
    } catch (error) {
      // Log the test result
      logger.error('Login demo test 5 failed', { test: 'Login demo test 5', error });
  
      // Rethrow the error so the test fails
      throw error;
    }
  });