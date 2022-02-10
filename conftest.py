import os
import json
import pytest
import platform

from typing import Dict
from botcity.web import WebBot, Browser, By
from botcity.web.browsers import edge

project_path = os.path.abspath('')


@pytest.fixture
def web(request):
    web = WebBot()
    web.headless = request.config.getoption("--headless")
    web.browser = request.config.getoption("--browser") or Browser.CHROME

    plt = platform.system()

    if web.browser == 'edge':
        if plt == 'Linux':
            opt = edge.default_options()
            opt.add_argument('--remote-debugging-port=9222')
            opt.add_argument('--no-sandbox')
            opt.add_argument('--disable-dev-shm-usage')
            opt.set_capability('platform', 'LINUX')  # WINDOWS is default value:
            web.options = opt
            web.driver_path = os.path.join(project_path, 'web-drivers', 'msedgedriver')
        elif plt == 'Windows':
            web.driver_path = os.path.join(project_path, 'web-drivers', 'msedgedriver.exe')

    elif web.browser == 'firefox':
        if plt == 'Linux':
            web.driver_path = os.path.join(project_path, 'web-drivers', 'geckodriver')
        elif plt == 'Windows':
            web.driver_path = os.path.join(project_path, 'web-drivers', 'geckodriver.exe')

    else:
        if plt == 'Linux':
            web.driver_path = os.path.join(project_path, 'web-drivers', 'chromedriver')
        elif plt == 'Windows':
            web.driver_path = os.path.join(project_path, 'web-drivers', 'chromedriver.exe')

    yield web

    web.stop_browser()


def get_event_result(id_event: str, web: WebBot) -> Dict:
    event_result = web.find_element(id_event, By.ID)
    return json.loads(event_result.text)


def pytest_addoption(parser):
    parser.addoption('--headless', action='store_const', const=True)
    parser.addoption('--browser', action='store', default='chrome')
