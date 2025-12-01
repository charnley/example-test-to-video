
import asyncio
from playwright.async_api import async_playwright
async def firefox_example():
    async with async_playwright() as p:
        # Launch Firefox browser
        browser = await p.firefox.launch(headless=False)
        
        # Create browser context and page
        context = await browser.new_context(
            record_video_dir="videos/"
        )
        page = await context.new_page()
        
        # Navigate to a webpage
        await page.goto("https://molcalc.org")
        
        # Wait for button to be visible and click it
        await page.wait_for_selector("#searchbar")
        
        await page.fill("#searchbar", "Propane")

        await page.press("#searchbar", "Enter")
        
        # Wait a moment to see the result
        await page.wait_for_timeout(2000)
        
        # Close browser
        context.close()
        await browser.close()


# Run the example
asyncio.run(firefox_example())
