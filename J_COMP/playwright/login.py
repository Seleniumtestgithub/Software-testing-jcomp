# GitHub_Login.py

# Code for GitHub login
import asyncio
import playwright
from playwright.async_api import async_playwright
from playwright.async_api import Error as PlaywrightError

# def inspect_page(username, password):
#     with sync_playwright() as p:
#         browser = p.firefox.launch()
#         context = browser.new_context()

#         # Open Playwright Inspector to visually inspect the page
#         with context.expect_event("page"):
#             page = context.new_page()
#             page.goto("https://github.com/login")
#             page.fill("input[name=login]", username)
#             page.fill("input[name=password]", password)
#             page.click("input[type=submit]")
#             page.pause()

async def github_login(username, password):

    async with async_playwright() as p:
        browser = await p.firefox.launch()
        context = await browser.new_context()

        try:
            page = await context.new_page()
            await page.goto("https://github.com/login")

            await page.fill("input[name=login]", username)
            await page.fill("input[name=password]", password)
            await page.click("input[type=submit]")

            #await page.wait_for_selector("img .avatar-user")
            try:
                page.wait_for_selector("button.sign-out", timeout=10000)
                print("Login successful!")
            except Exception:
                print("Login failed.")

        except PlaywrightError as e:
            raise Exception(f"Playwright error: {e}")

        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")

        finally:
            await browser.close()

if __name__ == '__main__':
    #inspect_page("Seleniumtestgithub", "throwawaygithub123")
    try:
        import logging
        logging.basicConfig(filename='automation.log', level=logging.DEBUG)
        logging.info("Starting the login process...")
        print("Starting the login process...")

        asyncio.run(github_login("Seleniumtestgithub", "throwawaygithub"))
        
    except Exception as e:
        print(f"Error: {str(e)}")
