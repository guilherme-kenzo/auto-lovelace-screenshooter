from .config import BASE_DIR
from ._download import download_driver_if_not_exists
from selenium import webdriver
from Screenshot import Screenshot_Clipping
import os


class ScreenshotClient:
    def __init__(self, url: str, driver_path: str = None, base_path: str = None):
        self.url = url
        self.driver_path = driver_path
        self.base_path = base_path
        self.driver = self._download_driver()

    def _download_driver(self):
        if download_driver_if_not_exists():
            return webdriver.Firefox(executable_path=self.driver_path)
        else:
            raise Exception(
                (
                    "Could not download driver. Try downloading it manually from https://github.com/mozilla/geckodriver/releases and place"
                    "it the correct location, which  is %s."
                )
                % os.path.join(self.base_dir, "geckodriver")
            )

    def navigate_to_page(self) -> None:
        webdriver.get(self.url)

    def _locate_elem(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def take_screenshot(self, xpath: str = None, output: str=None) -> None:
        elem = self._locate_elem(xpath)
        required_width = self.driver.execute_script('return document.body.parentNode.scrollWidth')
        required_height = self.driver.execute_script('return document.body.parentNode.scrollHeight')
        self.driver.set_window_size(required_width, required_height)
        self.driver.find_element_by_tag_name('body').screenshot(output)
