import asyncio
import time
from dataclasses import dataclass
from typing import Callable, Dict, List, Optional, Any
from playwright.async_api import async_playwright, Page, Browser, BrowserContext


@dataclass
class SectionTiming:
    name: str
    start_time: float
    end_time: float
    duration: float
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "duration": self.duration
        }


class TimedTestRunner:
    def __init__(self, page: Page):
        self.page = page
        self.timings: List[SectionTiming] = []
        
    async def run_section(self, name: str, section_func: Callable[[Page], Any]) -> SectionTiming:
        start_time = time.time()
        
        try:
            await section_func(self.page)
        except Exception as e:
            raise RuntimeError(f"Section '{name}' failed: {e}")
        
        end_time = time.time()
        duration = end_time - start_time
        
        timing = SectionTiming(
            name=name,
            start_time=start_time,
            end_time=end_time,
            duration=duration
        )
        
        self.timings.append(timing)
        return timing
    
    def get_timings(self) -> List[Dict[str, Any]]:
        return [timing.to_dict() for timing in self.timings]
    
    def clear_timings(self):
        self.timings.clear()


class VideoTutorialGenerator:
    def __init__(self, 
                 viewport_width: int = 1200,
                 viewport_height: int = 900,
                 slowmo: int = 100,
                 video_dir: str = "videos/"):
        self.viewport_width = viewport_width
        self.viewport_height = viewport_height
        self.slowmo = slowmo
        self.video_dir = video_dir
        self.browser: Optional[Browser] = None
        self.context: Optional[BrowserContext] = None
        self.page: Optional[Page] = None
        self.runner: Optional[TimedTestRunner] = None
        
    async def start(self, headless: bool = True) -> None:
        playwright = await async_playwright().__aenter__()
        
        self.browser = await playwright.chromium.launch(
            headless=headless, 
            slow_mo=self.slowmo
        )
        
        self.context = await self.browser.new_context(
            record_video_dir=self.video_dir,
            viewport={"width": self.viewport_width, "height": self.viewport_height},
            record_video_size={"width": self.viewport_width, "height": self.viewport_height},
        )
        
        self.page = await self.context.new_page()
        self.runner = TimedTestRunner(self.page)
        
    async def run_section(self, name: str, section_func: Callable[[Page], Any]) -> SectionTiming:
        if not self.runner:
            raise RuntimeError("Must call start() before running sections")
        return await self.runner.run_section(name, section_func)
        
    async def close(self) -> Dict[str, Any]:
        if not self.page or not self.context or not self.browser:
            raise RuntimeError("Must call start() before closing")
            
        video_path = await self.page.video.path()
        
        await self.context.close()
        await self.browser.close()
        
        timings = self.runner.get_timings() if self.runner else []
        
        return {
            "video_path": video_path,
            "timings": timings
        }
        
    def get_timings(self) -> List[Dict[str, Any]]:
        return self.runner.get_timings() if self.runner else []
