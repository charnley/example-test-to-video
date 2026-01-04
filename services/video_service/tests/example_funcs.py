import logging
from pathlib import Path

from playwright.sync_api import Page
from piper import PiperVoice

from tutorial_generator.page_funcs import human_like_select_and_fill
from tutorial_generator.video_funcs import generate_video
from tutorial_generator.speech_funcs import generate_audio
from tutorial_generator import generate_tutorial

logger = logging.getLogger(__name__)


def section_open_site(page: Page):
    page.goto("https://molcalc.org", timeout=60000)


def section_search_propane(page: Page):
    page.wait_for_selector("#searchbar")
    page.wait_for_timeout(2000)
    human_like_select_and_fill(page, "#searchbar", "Propane")
    page.press("#searchbar", "Enter")
    page.locator(".meter > span").wait_for(state="hidden")


def section_view_results(page: Page):

    page.get_by_role("link", name="Calculate Properties").scroll_into_view_if_needed()
    page.wait_for_timeout(3000)
    page.get_by_role("link", name="Calculate Properties").click()

    page.wait_for_timeout(3000)
    page.get_by_text("Indeed").click()

    page.wait_for_url("**/calculations/**")

    page.wait_for_timeout(3000)


def main2():

    video_name = "how_to_molcalc"

    sections = [
        ("open_site", section_open_site),
        ("search_propane", section_search_propane),
        ("view_results", section_view_results),
    ]

    times = generate_video(
        Path(video_name),
        sections,
    )

    print(times)

    # TODO Cut off the first loading of the website
    # TODO Split and add script


def main2():

    tmp_dir = Path("./tmp_videos")

    section_texts = [
        "Hi, I'm Amy",
        "Today we going to get quantum calculations gooooing",
    ]

    voice = PiperVoice.load("./voices/en_US-amy-medium.onnx")

    for i, text in enumerate(section_texts):

        filename = tmp_dir / f"section_{i}"
        filename = generate_audio(voice, text, filename)

        logger.info(f"Finished {filename}")

    return

def main():

    voice = PiperVoice.load("./voices/en_US-amy-medium.onnx")

    video_name = "how_to_molcalc"

    section_texts = [
        "Hi.",
        "Search for Propane",
        "View the results",
    ]

    section_actions = [
        section_open_site,
        section_search_propane,
        section_view_results,
    ]

    filename = generate_tutorial(video_name, voice, section_actions, section_texts, remove_first_section=True)

    return


if __name__ == "__main__":

    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    logger.info("Start molcalc example")

    main()

    logger.info("Finish molcalc example")
