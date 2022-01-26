import json
import os
from typing import Dict
import pytest

from botcity.web import WebBot, Browser, By


@pytest.fixture
def web() -> WebBot:
    project_path = os.path.abspath('')

    web = WebBot()
    web.headless = False
    web.browser = Browser.CHROME
    web.driver_path = os.path.join(project_path, 'web-drivers', 'chromedriver.exe')
    web.add_image('mouse', os.path.join(project_path, 'resources', 'mouse.png'))
    web.browse(os.path.join(project_path, 'web', 'index.html'))
    yield web

    web.stop_browser()


def get_event_result(id_event: str, web: WebBot) -> Dict:
    event_result = web.find_element(id_event, By.ID)
    return json.loads(event_result.text)


def test_left_click(web: WebBot):
    if not web.find("mouse", matching=0.97, waiting_time=10_000):
        raise Exception('Image not found: mouse')
    web.click()

    result = get_event_result('element-result', web)
    assert result['data'] == ['Left']


def test_left_double_click(web: WebBot):
    if not web.find("mouse", matching=0.97, waiting_time=10_000):
        raise Exception('Image not found: mouse')
    web.double_click()

    result = get_event_result('element-result', web)
    assert result['data'] == ['Left', 'Left']


def test_left_triple_click(web: WebBot):
    if not web.find("mouse", matching=0.97, waiting_time=10_000):
        raise Exception('Image not found: mouse')
    web.triple_click()

    result = get_event_result('element-result', web)
    assert result['data'] == ['Left', 'Left', 'Left']


def test_triple_click_reltive(web: WebBot):
    if not web.find("mouse", matching=0.97, waiting_time=10_000):
        raise Exception('Image not found: mouse')
    web.triple_click_relative(16, 140)

    result = get_event_result('element-result', web)
    assert result['data'] == ['Left2', 'Left2', 'Left2']


def test_right_click(web: WebBot):
    if not web.find("mouse", matching=0.97, waiting_time=10_000):
        raise Exception('Image not found: mouse')
    web.right_click()

    result = get_event_result('element-result', web)
    assert result['data'] == ['Right']


def test_right_double_click(web: WebBot):
    if not web.find("mouse", matching=0.97, waiting_time=10_000):
        raise Exception('Image not found: mouse')
    web.right_click(clicks=2)

    result = get_event_result('element-result', web)
    assert result['data'] == ['Right', 'Right']


def test_left_click_relative(web: WebBot):
    if not web.find("mouse", matching=0.97, waiting_time=10_000):
        raise Exception('Image not found: mouse')
    web.click_relative(16, 140)

    result = get_event_result('element-result', web)
    assert result['data'] == ['Left2']


def test_left_double_click_relative(web: WebBot):
    if not web.find("mouse", matching=0.97, waiting_time=10_000):
        raise Exception('Image not found: mouse')
    web.double_click_relative(16, 140)

    result = get_event_result('element-result', web)
    assert result['data'] == ['Left2', 'Left2']


def test_right_click_relative(web: WebBot):
    if not web.find("mouse", matching=0.97, waiting_time=10_000):
        raise Exception('Image not found: mouse')
    web.right_click_relative(16, 140)

    result = get_event_result('element-result', web)
    assert result['data'] == ['Right2']


def test_right_click_at(web: WebBot):
    web.right_click_at(170, 120)

    result = get_event_result('element-result', web)
    assert result['data'] == ['Right']


def test_get_last_x(web: WebBot):  # erro at @only_if_element
    if not web.find("mouse", matching=0.97, waiting_time=10_000):
        raise Exception('Image not found: mouse')
    web.move()

    web.move_to(100, 200)
    x = web.get_last_x()

    assert x == 100


def test_get_last_y(web: WebBot):
    if not web.find("mouse", matching=0.97, waiting_time=10_000):
        raise Exception('Image not found: mouse')
    web.move()

    web.move_to(100, 200)
    y = web.get_last_y()

    assert y == 200


def test_move_mouse(web: WebBot):
    if not web.find("mouse", matching=0.97, waiting_time=10_000):
        raise Exception('Image not found: mouse')
    web.move()

    result = get_event_result('element-result', web)
    assert result['data'] == ['mouse-over']


def test_move_relative(web: WebBot):
    if not web.find("mouse", matching=0.97, waiting_time=10_000):
        raise Exception('Image not found: mouse')
    web.move()  # posicionando o mouse
    web.move_relative(16, 140)

    result = get_event_result('element-result', web)
    assert result['data'] == ['mouse-over2']


def test_mouse_move(web: WebBot):
    web.mouse_move(170, 120)

    result = get_event_result('element-result', web)
    assert result['data'] == ['mouse-over']
