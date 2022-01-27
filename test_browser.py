import json
import os
import pytest

from typing import Dict
from PIL import Image
from botcity.web import WebBot, Browser, By
from selenium.webdriver.common.keys import Keys

project_path = os.path.abspath('')


@pytest.fixture
def web() -> WebBot:
    web = WebBot()
    web.headless = False
    web.browser = Browser.CHROME
    web.driver_path = os.path.join(project_path, 'web-drivers', 'chromedriver.exe')
    yield web

    web.stop_browser()


def get_event_result(id_event: str, web: WebBot) -> Dict:
    event_result = web.find_element(id_event, By.ID)
    return json.loads(event_result.text)


def test_create_tab(web: WebBot):
    web.browse(os.path.join(project_path, 'web', 'index.html'))
    web.create_tab('index.html')

    title = web.page_title()
    assert title == 'Botcity - web test'


def test_close_page(web: WebBot):
    web.browse(os.path.join(project_path, 'web', 'index.html'))
    web.create_tab('test.html')
    web.wait(5_000)
    web.close_page()

    title = web.page_title()
    assert title == 'Botcity - web test'


def test_create_window(web: WebBot):
    web.browse(os.path.join(project_path, 'web', 'index.html'))
    web.create_window(url='test.html')
    web.wait(2_000)

    title = web.page_title()
    assert title == 'Page test'


def test_display_size(web: WebBot):
    web.browse(os.path.join(project_path, 'web', 'index.html'))
    web.wait(2_000)
    (w, h) = web.display_size()

    assert (w, h) == (1600, 900)


def test_javascript(web: WebBot):
    web.browse(os.path.join(project_path, 'web', 'index.html'))
    web.execute_javascript("""
        document.getElementById('element-result').innerText = 'execute_javascript() works!';
    """)

    result = web.find_element('element-result', By.ID).text
    assert result == 'execute_javascript() works!'


def test_get_tabs(web: WebBot):
    web.browse(os.path.join(project_path, 'web', 'index.html'))
    web.create_tab('test.html')
    tabs = web.get_tabs()

    assert len(tabs) == 2


def test_navigate_to(web: WebBot):
    web.browse(os.path.join(project_path, 'web', 'index.html'))
    web.navigate_to(url=os.path.join(project_path, 'web', 'test.html'))
    web.wait(2_000)

    title = web.page_title()
    assert title == 'Page test'


def test_start_browser(web: WebBot):
    web.start_browser()
    tabs = web.get_tabs()

    assert len(tabs) == 1


def test_activate_tab(web: WebBot):
    web.browse(os.path.join(project_path, 'web', 'index.html'))
    web.create_tab('https://www.google.com')
    tabs = web.get_tabs()
    web.activate_tab(tabs[0])

    assert web.page_title() == 'Botcity - web test'


def test_get_image_from_map(web: WebBot):
    web.add_image('mouse', os.path.join(project_path, 'resources', 'mouse.png'))
    img = web.get_image_from_map('mouse')

    assert Image.isImageType(img)


def test_get_js_dialog(web: WebBot):
    web.browse(os.path.join(project_path, 'web', 'index.html'))
    web.type_keys([Keys.SHIFT, 'p'])

    alert = web.get_js_dialog()
    alert_text = alert.text
    alert.accept()  # alert must be closed before stop browser

    assert alert_text == 'Alert test'


def test_handle_js_dialog(web: WebBot):
    web.browse(os.path.join(project_path, 'web', 'index.html'))
    web.type_keys([Keys.SHIFT, 'l'])
    web.handle_js_dialog(prompt_text='Test input text')

    result = get_event_result('element-result', web)
    assert result['data'] == ['Test input text']


def test_get_screen_image(web: WebBot):
    web.browse(os.path.join(project_path, 'web', 'index.html'))
    img = web.get_screen_image(region=(0, 0, 400, 200))

    assert Image.isImageType(img)


def test_get_screenshot(web: WebBot):
    web.browse(os.path.join(project_path, 'web', 'index.html'))
    fp = os.path.join('resources', 'screenshot_test.png')
    img = web.get_screenshot(fp)

    assert Image.isImageType(img) and os.path.isfile(fp)
    os.remove(fp)
