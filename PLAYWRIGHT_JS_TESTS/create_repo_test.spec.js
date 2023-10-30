const { test, expect } = require('@playwright/test');
const winston = require('winston');
const axios = require('axios');
const token = "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";
const { login } = require('./login');
const repoName1 = "github-automation-p980";
const repoName2 = "github-automation-p981";

// Create a logger that writes to a file
const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.printf(info => `${info.timestamp} ${info.level}: ${info.message} [${info.test}] (${require('path').join(__dirname, 'tests')})`)
  ),
  defaultMeta: { service: 'user-service' },
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'combined.log' }),
  ],
});

test('Create repo test 1', async ({ page }) => {
  try {
    await login(page);

    try {
      const headers = { "Authorization": `token ${token}` };
      const data = { "name": repoName1 };
      const response = await axios.post("https://api.github.com/user/repos", data, { headers: headers });

      if (response.status === 201) {
        logger.info(`Repository '${repoName1}' created successfully.`, { test: 'Login demo test 1', file: __filename });
      } else {
        logger.error(`Failed to create repository. Status code: ${response.status}`, { test: 'Login demo test 1', file: __filename });
      }
    } catch (error) {
      logger.error(`Request error: ${error.toString()}`, { test: 'Login demo test 1', file: __filename });
      throw error;
    }
    // Log the test result
    logger.info('Create repo test 1 passed', { test: 'Create repo test 1', file: __filename });
  } catch (error) {
    // Log the test result
    logger.error('Create repo test 1 failed', { test: 'Create repo test 1', error, file: __filename });
    // Rethrow the error so the test fails
    throw error;
  }
});

test('Create repo test 2', async ({ page }) => {
  try {
    await login(page);

    try {
      const headers = { "Authorization": `token ${token}` };
      const data = { "name": repoName2 };
      const response = await axios.post("https://api.github.com/user/repos", data, { headers: headers });

      if (response.status === 201) {
        logger.info(`Repository '${repoName2}' created successfully.`, { test: 'Login demo test 1', file: __filename });
      } else {
        logger.error(`Failed to create repository. Status code: ${response.status}`, { test: 'Login demo test 1', file: __filename });
      }
    } catch (error) {
      logger.error(`Request error: ${error.toString()}`, { test: 'Login demo test 1', file: __filename });
      throw error;
    }
    // Log the test result
    logger.info('Create repo test 2 passed', { test: 'Create repo test 2', file: __filename });
  } catch (error) {
    // Log the test result
    logger.error('Create repo test 2 failed', { test: 'Create repo test 2', error, file: __filename });
    // Rethrow the error so the test fails
    throw error;
  }
});

test('Create repo test 3', async ({ page }) => {
  try {
    await login(page);

    try {
      const headers = { "Authorization": `token ${token}` };
      const data = { "name": repoName1 };
      const response = await axios.post("https://api.github.com/user/repos", data, { headers: headers });

      if (response.status === 201) {
        logger.info(`Repository '${repoName1}' created successfully.`, { test: 'Login demo test 1', file: __filename });
      } else {
        logger.error(`Failed to create repository. Status code: ${response.status}`, { test: 'Login demo test 1', file: __filename });
      }
    } catch (error) {
      logger.error(`Request error: ${error.toString()}`, { test: 'Login demo test 1', file: __filename });
      throw error;
    }
    // Log the test result
    logger.info('Create repo test 3 passed', { test: 'Create repo test 3', file: __filename });
  } catch (error) {
    // Log the test result
    logger.error('Create repo test 3 failed', { test: 'Create repo test 3', error, file: __filename });
    // Rethrow the error so the test fails
    throw error;
  }
});