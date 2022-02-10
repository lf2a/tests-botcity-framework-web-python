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

    if web.browser == 'edge':
        if platform.system() == 'Linux':
            opt = edge.default_options()
            opt.add_argument('--remote-debugging-port=9222')
            opt.set_capability('platform', 'LINUX')  # WINDOWS is default value:
            # opt.binary_location = '/usr/bin/microsoft-edge-stable'
            web.options = opt

        web.driver_path = os.path.join(project_path, 'web-drivers', 'msedgedriver')
    elif web.browser == 'firefox':
        web.driver_path = os.path.join(project_path, 'web-drivers', 'geckodriver')
    else:
        web.driver_path = os.path.join(project_path, 'web-drivers', 'chromedriver')
    yield web

    web.stop_browser()


def get_event_result(id_event: str, web: WebBot) -> Dict:
    event_result = web.find_element(id_event, By.ID)
    return json.loads(event_result.text)


def pytest_addoption(parser):
    parser.addoption('--headless', action='store_const', const=True)
    parser.addoption('--browser', action='store', default='chrome')
