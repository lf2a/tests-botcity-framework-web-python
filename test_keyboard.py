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


def test_control_a(web: WebBot):
    web.control_a()

    result = get_event_result('element-result', web)
    assert result['data'] == ['Control', 'a']


def test_control_c(web: WebBot):
    web.control_c()

    assert web.get_clipboard() == 'Botcity'


def test_enter(web: WebBot):
    web.enter()

    result = get_event_result('element-result', web)
    assert result['data'] == ['Enter']


def test_control_v(web: WebBot):
    web.copy_to_clipboard(text='botcity-paste')
    web.control_v()

    result = get_event_result('element-result', web)
    assert ''.join(result['data']) == 'botcity-paste'


def test_delete(web: WebBot):
    web.delete()

    result = get_event_result('element-result', web)
    assert result['data'] == ['Delete']


def test_key_end(web: WebBot):
    web.key_end()

    result = get_event_result('element-result', web)
    assert result['data'] == ['End']


def test_key_esc(web: WebBot):
    web.key_esc()

    result = get_event_result('element-result', web)
    assert result['data'] == ['Escape']


def test_key_home(web: WebBot):
    web.key_home()

    result = get_event_result('element-result', web)
    assert result['data'] == ['Home']


def test_type_keys(web: WebBot):
    web.type_keys(['a', 'b', 'c'])

    result = get_event_result('element-result', web)
    assert result['data'] == ['a', 'b', 'c']


def test_type_down(web: WebBot):
    web.type_down()

    result = get_event_result('element-result', web)
    assert result['data'] == ['ArrowDown']


def test_type_left(web: WebBot):
    web.type_left()

    result = get_event_result('element-result', web)
    assert result['data'] == ['ArrowLeft']


def test_type_right(web: WebBot):
    web.type_right()

    result = get_event_result('element-result', web)
    assert result['data'] == ['ArrowRight']


def test_type_up(web: WebBot):
    web.type_up()

    result = get_event_result('element-result', web)
    assert result['data'] == ['ArrowUp']


def test_backspace(web: WebBot):
    web.backspace()

    result = get_event_result('element-result', web)
    assert result['data'] == ['Backspace']


def test_hold_shift(web: WebBot):
    web.hold_shift()
    web.kb_type('a')
    web.release_shift()
    web.kb_type('a')

    result = get_event_result('element-result', web)
    assert result['data'] == ['Shift', 'A', 'a']


def test_space(web: WebBot):
    web.space()

    result = get_event_result('element-result', web)
    assert result['data'] == ['Space']


def test_page_down(web: WebBot):
    web.page_down()

    result = get_event_result('element-result', web)
    assert result['data'] == ['PageDown']


def test_page_up(web: WebBot):
    web.page_up()

    result = get_event_result('element-result', web)
    assert result['data'] == ['PageUp']


def test_key_tab(web: WebBot):
    web.tab()

    result = get_event_result('element-result', web)
    assert result['data'] == ['Tab']
