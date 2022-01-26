import json
import os
import pytest

from botcity.web import WebBot, Browser, By

project_path = os.path.abspath('')


@pytest.fixture
def web() -> WebBot:

    web = WebBot()
    web.headless = False
    web.browser = Browser.CHROME
    web.driver_path = os.path.join(project_path, 'web-drivers', 'chromedriver.exe')
    yield web

    web.stop_browser()


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
