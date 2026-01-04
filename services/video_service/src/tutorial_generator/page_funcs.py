from time import sleep
import random

from playwright.sync_api import Page


def highlight_element(page, selector):

    # TODO

    return


def slow_writing(
    page: Page,
    selector: str,
    text: str,
    min_delay: float = 0.05,
    max_delay: float = 0.15,
    has_mistakes=True,
):
    element = page.locator(selector)
    element.clear()
    element.click()

    for char in text:
        element.type(char, delay=0)
        delay = random.uniform(min_delay, max_delay)

        if random.random() < 0.1:
            delay += random.uniform(0.2, 0.5)

        if has_mistakes and random.random() < 0.05:
            wrong_char = random.choice("abcdefghijklmnopqrstuvwxyz")
            element.type(wrong_char, delay=0)
            sleep(random.uniform(0.1, 0.3))
            element.press("Backspace")
            sleep(random.uniform(0.1, 0.2))

        sleep(delay)


def human_like_select_and_fill(
    page: Page, selector: str, text: str, clear_first: bool = True
):
    element = page.locator(selector)
    element.wait_for(state="visible")
    sleep(random.uniform(0.1, 0.3))

    try:
        element.click()
    except Exception as _:
        element.focus()

    sleep(random.uniform(0.1, 0.2))

    if clear_first:
        element.press("Control+a")
        sleep(random.uniform(0.1, 0.2))
        element.press("Delete")
        sleep(random.uniform(0.1, 0.2))

    slow_writing(page, selector, text)
