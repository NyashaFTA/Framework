from dataclasses import dataclass

from core.browser.browser_type import BrowserType


@dataclass
class BrowserConfig:

    browser: BrowserType = BrowserType.CHROME

    mobile: bool = False

    headless: bool = False