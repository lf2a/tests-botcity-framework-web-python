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
BROWSER = Browser.CHROME


def setup_chrome(headless: bool) -> WebBot:
    web = WebBot(headless)
    web.browser = Browser.CHROME

    if OS_NAME == 'Windows':
        web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'windows', 'chromedriver.exe')
    elif OS_NAME == 'Linux':
        web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'linux', 'chromedriver')
    elif OS_NAME == 'Darwin':
        web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'macos', 'chromedriver')
    else:
        raise ValueError(f'OS [{OS_NAME}] not supported.')

    return web


def setup_firefox(headless: bool) -> WebBot:
    web = WebBot(headless)
    web.browser = Browser.FIREFOX

    if OS_NAME == 'Windows':
        web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'windows', 'geckodriver.exe')
    elif OS_NAME == 'Linux':
        web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'linux', 'geckodriver')
    elif OS_NAME == 'Darwin':
        web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'macos', 'geckodriver')
    else:
        raise ValueError(f'OS [{OS_NAME}] not supported.')

    return web


def setup_edge(headless: bool) -> WebBot:
    web = WebBot(headless=headless)
    web.browser = Browser.EDGE

    opt = edge.default_options(headless=headless, download_folder_path=web.download_folder_path)
    opt.set_capability('platform', 'ANY')  # WINDOWS is default value:

    if OS_NAME == 'Windows':
        web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'windows', 'msedgedriver.exe')
    elif OS_NAME == 'Linux':
        opt.add_argument('--remote-debugging-port=9222')
        web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'linux', 'msedgedriver')
    elif OS_NAME == 'Darwin':
        web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'macos', 'msedgedriver')
    else:
        raise ValueError(f'OS [{OS_NAME}] not supported.')

    web.options = opt
    return web


@pytest.fixture
def web(request):
    global BROWSER
    BROWSER = request.config.getoption("--browser") or Browser.CHROME

    is_headless = request.config.getoption("--headless")

    if BROWSER == 'chrome':
        web = setup_chrome(is_headless)
    elif BROWSER == 'firefox':
        web = setup_firefox(is_headless)
    elif BROWSER == 'edge':
        web = setup_edge(is_headless)
    else:
        raise ValueError(f'Browser [browser] not supported.')

    yield web
    web.stop_browser()


def get_event_result(id_event: str, web: WebBot) -> typing.Dict:
    event_result = web.find_element(id_event, By.ID)
    return json.loads(event_result.text)


def pytest_addoption(parser):
    parser.addoption('--headless', action='store_const', const=True)
    parser.addoption('--browser', action='store', default='chrome')
