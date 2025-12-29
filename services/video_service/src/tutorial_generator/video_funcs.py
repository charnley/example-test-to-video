from pathlib import Path
from typing import Callable
from playwright.async_api import async_playwright, Page, Browser, BrowserContext

from tutorial_generator.constants import (
    DEFAULT_VIEWPOINT_WIDTH,
    DEFAULT_VIEWPOINT_HEIGHT,
)

async def generate_video(
    video_filename: Path,
    sections: list[tuple[str, Callable[[Page], None]]],
    viewport_width: int = DEFAULT_VIEWPOINT_WIDTH,
    viewport_height: int = DEFAULT_VIEWPOINT_HEIGHT,
    slowmo: int = 100,
    work_dir: str = Path("tmp_videos/")
):

    playwright = await async_playwright()

    browser = await playwright.chromium.launch(
        headless=headless,
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

    generated_video_path = await self.page.video.path()

    await self.context.close()
    await self.browser.close()

    # Rename video with segment name
    new_video_path = video_filename.parent / f"{video_filename.stem}{generated_video_path.suffix}"
    generated_video_path.rename(new_video_path)

    logger.info("Video renamed")

    return timings
