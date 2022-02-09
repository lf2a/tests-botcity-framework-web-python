import os
import json
import pytest

from typing import Dict
from botcity.web import WebBot, Browser, By

project_path = os.path.abspath('')


@pytest.fixture
def web(request):
    web = WebBot()
    web.headless = request.config.getoption("--headless")

    web.browser = request.config.getoption("--browser") or Browser.CHROME
    if web.browser == 'edge':
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