import logging
import time
from pathlib import Path
from typing import Callable

import playwright
# from playwright.async_api import Page, async_playwright
from playwright.sync_api import sync_playwright, Page
from tutorial_generator.constants import DEFAULT_VIEWPOINT_HEIGHT, DEFAULT_VIEWPOINT_WIDTH

logger = logging.getLogger(__name__)


def generate_video(
    video_filename: Path,
    sections: list[Callable[[Page], None]],
    viewport_width: int = DEFAULT_VIEWPOINT_WIDTH,
    viewport_height: int = DEFAULT_VIEWPOINT_HEIGHT,
    slowmo: int = 100,
    work_dir: Path = Path("tmp_videos/"),
):
    """
    Returns timings based on the video length
    """

    # playwright = async_playwright().__aenter__()

    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(
        headless=True,
        slow_mo=slowmo,
    )

    context = browser.new_context(
        record_video_dir=work_dir,
        viewport={"width": viewport_width, "height": viewport_height},
        record_video_size={"width": viewport_width, "height": viewport_height},
    )

    page = context.new_page()

    # Init done, now run sections and time it
    timings = []

    start_time = time.time()

    for section_func in sections:

        section_start_time = time.time()

        section_func(page)

        section_end_time = time.time()
        timings.append(section_end_time - start_time)

        duration = section_end_time - section_start_time
        logger.info(f"Section {section_func.__name__} took {duration:.2f} sec")

    logger.info("Saving video")

    generated_video_path = page.video.path()

    context.close()
    browser.close()
    playwright.stop()

    generated_video_path = Path(generated_video_path)

    # Rename video with segment name
    new_video_path = generated_video_path.parent / f"{video_filename.stem}{generated_video_path.suffix}"
    generated_video_path.rename(new_video_path)

    logger.info(f"Video renamed: {generated_video_path}")

    return timings
