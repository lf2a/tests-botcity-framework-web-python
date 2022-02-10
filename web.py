import os

from botcity.web import WebBot, Browser, browsers

print(os.path.abspath(''))
print(os.path.exists(os.path.join(os.path.abspath(''), 'web-drivers', 'msedgedriver')))

web = WebBot()
web.headless = True
web.browser = Browser.EDGE
web.driver_path = os.path.join(os.path.abspath(''), 'web-drivers', 'msedgedriver')

opt = browsers.edge.default_options()
opt.add_argument('--remote-debugging-port=9222')
opt.add_argument('--no-sandbox')
opt.add_argument('--disable-dev-shm-usage')
opt.set_capability('platform', 'LINUX')  # WINDOWS is default value:
opt.binary_location = '/usr/bin/microsoft-edge-stable'
web.options = opt

web.browse('https://google.com')
web.wait(5_000)
web.stop_browser()
