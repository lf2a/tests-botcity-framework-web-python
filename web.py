import os

print(os.path.abspath(''))
print(os.path.exists(os.path.join(os.path.abspath(''), 'web-drivers', 'chromedriver')))
