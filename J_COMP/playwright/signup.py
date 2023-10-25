# GitHub_Signup.py

# Code for GitHub signup
import asyncio
from playwright.sync_api import async_playwright
from playwright.sync_api import Error as PlaywrightError

async def github_signup(username, password, email):
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()

        try:
            page = await context.new_page()
            await page.goto("https://github.com/join")

            await page.fill("input[name=login]", username)
            await page.fill("input[name=email]", email)
            await page.fill("input[name=password]", password)
            await page.click("button[type=submit]")

            await page.wait_for_selector("div.error")
            error_message = await get_element_text(page, "div.error")

            if "CAPTCHA" in error_message:
                raise Exception("CAPTCHA encountered. Manual intervention required.")
            else:
                print("Sign-up successful!")

        except PlaywrightError as e:
            raise Exception(f"Playwright error: {e}")

        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")

        finally:
            await browser.close()

if __name__ == '__main__':
    try:
        asyncio.run(github_signup("Seleniumtestgithub2", "throwawaygithub", "Email@example.com"))
    except Exception as e:
        print(f"Error: {str(e)}")
