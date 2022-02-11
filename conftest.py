import os
import json
import pytest
import platform
import typing

from botcity.web import WebBot, Browser, By
from botcity.web.browsers import edge

PROJECT_DIR = os.path.abspath('')
INDEX_PAGE = 'file://' + os.path.join(PROJECT_DIR, 'web', 'index.html')
TEST_PAGE = 'file://' + os.path.join(PROJECT_DIR, 'web', 'test.html')
OS_NAME = platform.system()


@pytest.fixture
def web(request):
    web = WebBot()
    web.headless = request.config.getoption("--headless")
    web.browser = request.config.getoption("--browser") or Browser.CHROME

    if web.browser == 'edge':
        if OS_NAME == 'Linux':
            opt = edge.default_options()
            opt.add_argument('--remote-debugging-port=9222')
            opt.add_argument('--no-sandbox')
            opt.add_argument('--disable-dev-shm-usage')
            opt.set_capability('platform', 'LINUX')  # WINDOWS is default value:
            web.options = opt
            web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'linux', 'msedgedriver')
        elif OS_NAME == 'Windows':
            web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'windows', 'msedgedriver.exe')
        elif OS_NAME == 'Darwin':
            opt = edge.default_options()
            opt.set_capability('platform', 'MAC')  # WINDOWS is default value:
            web.options = opt
            web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'macos', 'msedgedriver')

    elif web.browser == 'firefox':
        if OS_NAME == 'Linux':
            web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'linux', 'geckodriver')
        elif OS_NAME == 'Windows':
            web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'windows', 'geckodriver.exe')
        elif OS_NAME == 'Darwin':
            web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'macos', 'geckodriver')

    else:
        if OS_NAME == 'Linux':
            web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'linux', 'chromedriver')
        elif OS_NAME == 'Windows':
            web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'windows', 'chromedriver.exe')
        elif OS_NAME == 'Darwin':
            web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'macos', 'chromedriver')

    yield web

    web.stop_browser()


def get_event_result(id_event: str, web: WebBot) -> typing.Dict:
    event_result = web.find_element(id_event, By.ID)
    return json.loads(event_result.text)


def pytest_addoption(parser):
    parser.addoption('--headless', action='store_const', const=True)
    parser.addoption('--browser', action='store', default='chrome')
