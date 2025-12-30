import logging
import time
from pathlib import Path
from typing import Callable

from playwright.async_api import Page, async_playwright
from tutorial_generator.constants import DEFAULT_VIEWPOINT_HEIGHT, DEFAULT_VIEWPOINT_WIDTH

logger = logging.getLogger(__name__)


async def generate_video(
    video_filename: Path,
    sections: list[tuple[str, Callable[[Page], None]]],
    viewport_width: int = DEFAULT_VIEWPOINT_WIDTH,
    viewport_height: int = DEFAULT_VIEWPOINT_HEIGHT,
    slowmo: int = 100,
    work_dir: str = Path("tmp_videos/"),
):

    playwright = await async_playwright().__aenter__()

    browser = await playwright.chromium.launch(
        headless=True,
        slow_mo=slowmo,
    )

    context = await browser.new_context(
        record_video_dir=work_dir,
        viewport={"width": viewport_width, "height": viewport_height},
        record_video_size={"width": viewport_width, "height": viewport_height},
    )

    page = await context.new_page()

    # Init done, now run sections and time it
    timings = []

    start_time = time.time()

    for section_name, section_func in sections:

        section_start_time = time.time()

        await section_func(page)

        section_end_time = time.time()
        timings.append(section_end_time)

        duration = section_end_time - section_start_time

        logging.info(f"Section: '{section_name}' took {duration:.2f} sec")

    logger.info("Saving video")

    generated_video_path = await page.video.path()
    generated_video_path = Path(generated_video_path)

    await context.close()
    await browser.close()

    # Rename video with segment name
    new_video_path = video_filename.parent / f"{video_filename.stem}{generated_video_path.suffix}"
    generated_video_path.rename(new_video_path)

    logger.info(f"Video renamed: {generated_video_path}")

    return timings
