import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose lang")


@pytest.fixture(scope="function")
def browser(request):
    lang1 = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang1})
    browser = webdriver.Chrome(options=options)
        
    yield browser
    print("\nquit browser..")
    time.sleep(30)
    browser.quit()
