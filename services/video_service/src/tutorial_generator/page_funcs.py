import asyncio
import random

from playwright.async_api import Page


async def highlight_element(page, selector):

    # TODO

    return


async def slow_writing(
    page: Page,
    selector: str,
    text: str,
    min_delay: float = 0.05,
    max_delay: float = 0.15,
    has_mistakes=True,
):
    element = page.locator(selector)
    await element.clear()
    await element.click()

    for char in text:
        await element.type(char, delay=0)
        delay = random.uniform(min_delay, max_delay)

        if random.random() < 0.1:
            delay += random.uniform(0.2, 0.5)

        if has_mistakes and random.random() < 0.05:
            wrong_char = random.choice("abcdefghijklmnopqrstuvwxyz")
            await element.type(wrong_char, delay=0)
            await asyncio.sleep(random.uniform(0.1, 0.3))
            await element.press("Backspace")
            await asyncio.sleep(random.uniform(0.1, 0.2))

        await asyncio.sleep(delay)


async def human_like_select_and_fill(
    page: Page, selector: str, text: str, clear_first: bool = True
):
    element = page.locator(selector)
    await element.wait_for(state="visible")
    await asyncio.sleep(random.uniform(0.1, 0.3))

    try:
        await element.click()
    except Exception as _:
        await element.focus()

    await asyncio.sleep(random.uniform(0.1, 0.2))

    if clear_first:
        await element.press("Control+a")
        await asyncio.sleep(random.uniform(0.1, 0.2))
        await element.press("Delete")
        await asyncio.sleep(random.uniform(0.1, 0.2))

    await slow_writing(page, selector, text)
