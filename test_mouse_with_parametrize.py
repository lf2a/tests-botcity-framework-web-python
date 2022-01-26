import json
import os
from typing import Dict
import pytest

from botcity.web import WebBot, Browser, By

PROJECT_PATH = os.path.abspath('')


@pytest.mark.parametrize("headless,driver,browser", [
    (False, Browser.FIREFOX, 'geckodriver.exe'),
    (True, Browser.FIREFOX, 'geckodriver.exe'),
    (False, Browser.CHROME, 'chromedriver.exe'),
    (True, Browser.CHROME, 'chromedriver.exe'),
    (False, Browser.EDGE, 'msedgedriver.exe'),
    (True, Browser.EDGE, 'msedgedriver.exe')
])
class TestMouse:

    def setup_web_bot(self, headless, driver, browser):
        web = WebBot()
        web.headless = headless
        web.browser = driver
        web.driver_path = os.path.join(PROJECT_PATH, 'web-drivers', browser)
        web.add_image('mouse', os.path.join(PROJECT_PATH, 'resources', 'mouse.png'))
        web.browse(os.path.join(PROJECT_PATH, 'web', 'index.html'))
        web.set_screen_resolution(1280, 720)
        return web

    def get_event_result(self, id_event: str, web: WebBot) -> Dict:
        event_result = web.find_element(id_event, By.ID)
        return json.loads(event_result.text)

    def test_left_click(self, headless, driver, browser):
        web = self.setup_web_bot(headless, driver, browser)
        if not web.find("mouse", matching=0.97, waiting_time=10_000):
            raise Exception('Image not found: mouse')
        web.click()

        result = self.get_event_result('element-result', web)
        web.stop_browser()
        assert result['data'] == ['Left']
