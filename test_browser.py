import os
import conftest

from PIL import Image
from botcity.web import WebBot, Browser, By


def test_create_tab(web: WebBot):
    web.start_browser()
    web.create_tab('https://github.com/botcity-dev/botcity-framework-web-python')
    web.wait(2_000)

    title = web.page_title()
    assert 'botcity-framework-web-python: BotCity Framework Web' in title


def test_close_page(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    web.create_tab('test.html')
    web.wait(5_000)
    web.close_page()

    title = web.page_title()
    assert title == 'Botcity - web test'


def test_create_window(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    web.create_window(url='test.html')
    web.wait(2_000)

    title = web.page_title()
    assert title == 'Page test'


def test_display_size(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    web.set_screen_resolution(1280, 720)
    (w, h) = web.display_size()

    assert (w, h) == (1280, 720)


def test_javascript(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    web.execute_javascript("""
        document.getElementById('element-result').innerText = 'execute_javascript() works!';
    """)

    result = web.find_element('element-result', By.ID).text
    assert result == 'execute_javascript() works!'


def test_get_tabs(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    web.create_tab('test.html')
    tabs = web.get_tabs()

    assert len(tabs) == 2


def test_navigate_to(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    web.navigate_to(url='file://' + os.path.join(conftest.project_path, 'web', 'test.html'))
    web.wait(2_000)

    title = web.page_title()
    assert title == 'Page test'


def test_start_browser(web: WebBot):
    web.start_browser()
    tabs = web.get_tabs()

    assert len(tabs) == 1


def test_activate_tab(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    web.create_tab('https://www.google.com')
    tabs = web.get_tabs()
    web.activate_tab(tabs[0])

    assert web.page_title() == 'Botcity - web test'


def test_get_image_from_map(web: WebBot):
    web.add_image('mouse', os.path.join(conftest.project_path, 'resources', 'mouse.png'))
    img = web.get_image_from_map('mouse')

    assert Image.isImageType(img)


def test_get_js_dialog(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    web.type_keys([web.KEYS.SHIFT, 'p'])

    alert = web.get_js_dialog()
    alert_text = alert.text
    alert.accept()  # alert must be closed before stop browser

    assert alert_text == 'Alert test'


def test_handle_js_dialog(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    web.type_keys([web.KEYS.SHIFT, 'l'])
    web.handle_js_dialog(prompt_text='Test input text')

    result = conftest.get_event_result('element-result', web)
    assert result['data'] == ['Test input text']


def test_get_screen_image(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    img = web.get_screen_image(region=(0, 0, 400, 200))

    assert Image.isImageType(img)


def test_get_screenshot(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    fp = os.path.join('resources', 'screenshot_test.png')
    img = web.get_screenshot(fp)

    assert Image.isImageType(img) and os.path.isfile(fp)
    os.remove(fp)


def test_screen_cut(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    fp = os.path.join('resources', 'screen_cut_test.png')
    img = web.screen_cut(0, 0, 100, 200)
    img.save(fp)

    assert Image.isImageType(img) and os.path.isfile(fp)
    os.remove(fp)


def test_find_element(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    element = web.find_element('botcity', By.ID)

    assert element.text == 'Botcity'


def test_find_elements(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    elements = web.find_elements('botcity', By.ID)

    assert [element.text for element in elements] == ['Botcity']


def test_maximize_window(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    web.maximize_window()

    is_maximized = web.find_element('is-maximized', By.ID)
    assert is_maximized


def test_page_source(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    page = web.page_source()

    assert page.title.text == 'Botcity - web test'


def test_set_file_input_element(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    input_file_element = web.find_element('file', By.ID)

    pdf_file = os.path.join(conftest.project_path, 'web', 'sample.pdf')
    web.set_file_input_element(input_file_element, pdf_file)
    web.wait(5_000)

    file_name = os.path.basename(input_file_element.get_attribute('value'))
    assert file_name == 'C:\\fakepath\\sample.pdf'


def test_enter_iframe(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    iframe = web.find_element('pgtest', By.ID)
    web.enter_iframe(iframe)

    bs = web.page_source()
    assert bs.title.text == 'Page test'


def test_leave_iframe(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    iframe = web.find_element('pgtest', By.ID)
    web.enter_iframe(iframe)
    web.leave_iframe()

    bs = web.page_source()
    assert bs.title.text == 'Botcity - web test'


def test_get_view_port_size(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    size = web.get_viewport_size()

    element = web.find_element('window-size', By.ID).text.split('x')
    assert size == tuple(int(e) for e in element)


def test_scroll_down(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    web.add_image('python', os.path.join(conftest.project_path, 'resources', 'python.png'))
    web.scroll_down(20)

    python_icon = web.find("python", matching=0.97, waiting_time=10000)
    assert python_icon is not None


def test_scroll_up(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    web.add_image('mouse', os.path.join(conftest.project_path, 'resources', 'mouse.png'))
    web.type_keys([web.KEYS.SHIFT, 'd'])  # scroll down trigger
    web.scroll_up(20)

    mouse_icon = web.find("mouse", matching=0.97, waiting_time=10_000)
    assert mouse_icon is not None


def test_set_screen_resolution(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    web.set_screen_resolution(1280, 720)

    page_size = web.find_element('page-size', By.ID).text
    window_size = web.find_element('window-size', By.ID).text

    if web.browser == Browser.FIREFOX and web.headless:
        # Firefox remove complete browser window including its decorations and title bar
        assert window_size == '1280x720'
    else:
        assert page_size == '1280x720'


def test_wait_for_downloads(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    web.wait(1000)

    web.type_keys([web.KEYS.SHIFT, 'q'])
    web.wait(1000)

    web.wait_for_downloads()

    file_name = '10MB.bin'
    file = os.path.join(conftest.project_path, file_name)
    # if *.part exists download is not complete.
    file_part = os.path.join(conftest.project_path, file_name + '.part')

    assert os.path.isfile(file) and not os.path.exists(file_part)
    os.remove(file)


def test_wait_for_file(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    web.wait(1000)

    web.type_keys([web.KEYS.SHIFT, 'q'])
    web.wait(5000)

    file = os.path.join(conftest.project_path, '10MB.bin')
    file_part = os.path.join(conftest.project_path, '10MB.bin.part')  # if *.part exists download is not complete.

    assert web.wait_for_file(file) and os.path.isfile(file) and not os.path.exists(file_part)
    web.wait(2000)
    os.remove(file)


def test_set_current_element(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    web.wait(1000)

    web.add_image('mouse', os.path.join(conftest.project_path, 'resources', 'mouse.png'))
    web.add_image('git', os.path.join(conftest.project_path, 'resources', 'git.png'))

    mouse_element = web.find("mouse", matching=0.97, waiting_time=10_000)

    if not web.find("git", matching=0.97, waiting_time=10000):
        raise Exception('Image not found: git')
    web.click(wait_after=2000)

    web.set_current_element(mouse_element)
    web.click(wait_after=2000)

    result = conftest.get_event_result('element-result', web)
    assert result['data'] == ['Left']


def test_print_pdf(web: WebBot):
    web.browse('file://' + os.path.join(conftest.project_path, 'web', 'index.html'))
    pdf = web.print_pdf(path=os.path.join(conftest.project_path, 'page.pdf'))

    assert os.path.exists(pdf)
    os.remove(pdf)
