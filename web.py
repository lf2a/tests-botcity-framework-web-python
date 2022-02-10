import os

from botcity.web import WebBot, Browser, browsers
from selenium.webdriver import DesiredCapabilities

print(os.path.abspath(''))
print(os.path.exists(os.path.join(os.path.abspath(''), 'web-drivers', 'msedgedriver')))

web = WebBot()
web.headless = True
web.browser = Browser.EDGE
web.driver_path = os.path.join(os.path.abspath(''), 'web-drivers', 'msedgedriver')

opt = browsers.edge.default_options()
opt.add_argument('--remote-debugging-port=9222')
opt.add_argument('--no-sandbox')
opt.add_argument('--disable-setuid-sandbox')
opt.set_capability('platform', 'LINUX')  # WINDOWS is default value:
opt.binary_location = '/usr/bin/microsoft-edge-stable'
opt.use_chromium = True
web.options = opt

# cap = DesiredCapabilities.EDGE.copy()
# cap['platform'] = 'LINUX'
# web.capabilities = cap

web.browse('https://google.com')
web.wait(5_000)
web.stop_browser()
