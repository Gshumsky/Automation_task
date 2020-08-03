import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='choose language')

@pytest.fixture(scope='function')
def browser(request):
    language=request.config.getoption('language')
    options2 = Options()
    options2.add_experimental_option('prefs', {'intl.accept_languages': language})
    #создал опцию
    print('\nStarting chrome')
    browser=webdriver.Chrome(options=options2)
    yield browser
    time.sleep(4)
    print("\nquit browser..")
    browser.quit()
