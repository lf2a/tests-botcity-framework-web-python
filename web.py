import os
import logging
import conftest

from botcity.web import WebBot, Browser

# web = WebBot()
# web.headless = True
# web.browser = Browser.EDGE
# web.driver_path = os.path.join(os.path.abspath(''), 'web-drivers', 'windows', 'msedgedriver.exe')


def test_a(web: WebBot):
    web.browse('https://google.com')
    web.wait(5_000)


LOGGER = logging.getLogger(__name__)
LOGGER.info(conftest.BROWSER)
