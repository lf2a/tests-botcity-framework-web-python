import json
import os
from typing import Dict
import pytest

from botcity.web import WebBot, Browser, By

project_path = os.path.abspath('')


@pytest.fixture
def web() -> WebBot:
    web = WebBot()
    web.headless = False
    web.browser = Browser.CHROME
    web.driver_path = os.path.join(project_path, 'web-drivers', 'chromedriver.exe')
    # web.driver_path = os.path.join(project_path, 'web-drivers', 'geckodriver.exe')
    # web.driver_path = os.path.join(project_path, 'web-drivers', 'msedgedriver.exe')
    web.browse(os.path.join(project_path, 'web', 'index.html'))
    yield web

    web.stop_browser()


def get_event_result(id_event: str, web: WebBot) -> Dict:
    event_result = web.find_element(id_event, By.ID)
    return json.loads(event_result.text)


def test_find_one(web: WebBot):
    web.add_image('mario4', os.path.join(project_path, 'resources', 'mario4.png'))
    if not web.find("mario4", matching=0.97, waiting_time=10_000):
        raise Exception('Image not found: mario4')
    web.click()

    result = get_event_result('element-result', web)
    assert result['data'] == ['img04']


def test_find_all(web: WebBot):
    web.add_image('mario5', os.path.join(project_path, 'resources', 'mario5.png'))
    marios = web.find_all("mario5", matching=0.97, waiting_time=10_000)

    elements = []
    for m in marios:
        web.click()
        result = get_event_result('element-result', web)
        elements.append(result['data'])

    assert elements == [['img05'], ['img06'], ['img07'], ['img08']]


def test_get_last_element(web: WebBot):
    web.add_image('mario5', os.path.join(project_path, 'resources', 'mario5.png'))
    ele = web.find('mario5')

    assert ele is not None


def test_find_text(web: WebBot):
    web.add_image('hello_world', os.path.join(project_path, 'resources', 'hello_world.png'))
    ele = web.find("hello_world", matching=0.97, waiting_time=10000)

    assert ele is not None


def test_find_multiple(web: WebBot):
    web.add_image('mario3', os.path.join('resources', 'mario3.png'))
    web.add_image('mario4', os.path.join('resources', 'mario4.png'))
    images = web.find_multiple(labels=['mario3', 'mario4'])

    assert None not in (images['mario3'], images['mario4'])
