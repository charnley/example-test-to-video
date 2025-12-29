from playwright.async_api import async_playwright, Page, Browser, BrowserContext
import asyncio
from pathlib import Path
import logging

from tutorial_generator.page_funcs import human_like_select_and_fill
from tutorial_generator.video_funcs import generate_video

logger = logging.getLogger(__name__)


async def section_open_site(page: Page):
    await page.goto("https://molcalc.org", timeout=60000)


async def section_search_propane(page: Page):
    await page.wait_for_selector("#searchbar")
    await page.wait_for_timeout(2000)
    await human_like_select_and_fill(page, "#searchbar", "Propane")
    await page.press("#searchbar", "Enter")
    await page.locator(".meter > span").wait_for(state="hidden")


async def section_view_results(page: Page):

    await page.wait_for_timeout(3000)
    await page.get_by_role("link", name="Calculate Properties").scroll_into_view_if_needed()
    await page.get_by_role("link", name="Calculate Properties").click()

    await page.wait_for_timeout(3000)
    await page.get_by_text("Indeed").click()

    await page.wait_for_timeout(3000)


async def main():

    video_name = "how_to_molcalc"

    sections = [
        ("open_site", section_open_site),
        ("search_propane", section_search_propane),
        ("view_results", section_view_results)
    ]

    times = await generate_video(
        Path(video_name),
        sections,
    )

    print(times)

    # TODO Cut off the first loading of the website
    # TODO Split and add script

if __name__ == "__main__":

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    logger.info("Start molcalc example")

    asyncio.run(main())

    logger.info("Finish molcalc example")
