# import asyncio
# from playwright.async_api import async_playwright

# async def github_login(username, password):
#     async with async_playwright() as p:
#         browser = await p.chromium.launch()
#         context = await browser.new_context()

#         page = await context.new_page()
#         await page.goto("https://github.com/login")

#         await page.fill("input[name=login]", username)
#         await page.fill("input[name=password]", password)
#         await page.click("input[type=submit]")

#         # Add assertions or further actions as needed

#         await browser.close()

# if __name__ == '__main__':
#     asyncio.run(github_login("YourUsername", "YourPassword"))

import win32com.client as comclt
wsh= comclt.Dispatch("WScript.Shell")
#  wsh.AppActivate("Notepad") # select another application
wsh.SendKeys("{tab}") # send the keys you want