import os
import json
import pytest
import typing
import platform

from botcity.web import WebBot, Browser, By, browsers

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

OS_NAME = platform.system()

PROJECT_DIR = os.path.abspath('')
TEST_PAGE = 'file://' + os.path.join(PROJECT_DIR, 'web', 'test.html').replace('\\', '/')
INDEX_PAGE = 'file://' + os.path.join(PROJECT_DIR, 'web', 'index.html').replace('\\', '/')


def setup_chrome(headless: bool) -> WebBot:
    web = WebBot(headless)
    web.browser = Browser.CHROME
    web.driver_path = ChromeDriverManager().install()

    # if OS_NAME == 'Windows':
    #     web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'windows', 'chromedriver.exe')
    # elif OS_NAME == 'Linux':
    #     web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'linux', 'chromedriver')
    # elif OS_NAME == 'Darwin':
    #     web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'macos', 'chromedriver')
    # else:
    #     raise ValueError(f'OS [{OS_NAME}] not supported.')
    return web


def setup_firefox(headless: bool) -> WebBot:
    web = WebBot(headless)
    web.browser = Browser.FIREFOX
    web.driver_path = GeckoDriverManager().install()

    # if OS_NAME == 'Windows':
    #     web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'windows', 'geckodriver.exe')
    # elif OS_NAME == 'Linux':
    #     web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'linux', 'geckodriver')
    # elif OS_NAME == 'Darwin':
    #     web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'macos', 'geckodriver')
    # else:
    #     raise ValueError(f'OS [{OS_NAME}] not supported.')
    return web


def setup_edge(headless: bool) -> WebBot:
    web = WebBot(headless)
    web.browser = Browser.EDGE

    opt = browsers.edge.default_options(headless=headless, download_folder_path=web.download_folder_path)
    opt.set_capability('platform', 'ANY')  # WINDOWS is default value:
    web.driver_path = EdgeChromiumDriverManager().install()

    # if OS_NAME == 'Windows':
    #     web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'windows', 'msedgedriver.exe')
    # elif OS_NAME == 'Linux':
    #     opt.add_argument('--remote-debugging-port=9222')
    #     web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'linux', 'msedgedriver')
    # elif OS_NAME == 'Darwin':
    #     web.driver_path = os.path.join(PROJECT_DIR, 'web-drivers', 'macos', 'msedgedriver')
    # else:
    #     raise ValueError(f'OS [{OS_NAME}] not supported.')
    web.options = opt
    return web


@pytest.fixture
def web(request):

    browser = request.config.getoption("--browser") or Browser.CHROME
    is_headless = request.config.getoption("--headless")

    if browser == 'chrome':
        web = setup_chrome(is_headless)
    elif browser == 'firefox':
        web = setup_firefox(is_headless)
    elif browser == 'edge':
        web = setup_edge(is_headless)
    else:
        raise ValueError(f'Browser [{browser}] not supported.')
    yield web
    web.stop_browser()


def get_event_result(id_event: str, web: WebBot) -> typing.Dict:
    event_result = web.find_element(id_event, By.ID)
    return json.loads(event_result.text)


def pytest_addoption(parser):
    parser.addoption('--headless', action='store_const', const=True)
    parser.addoption('--browser', action='store', default='chrome')
