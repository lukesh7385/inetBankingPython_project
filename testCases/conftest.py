from selenium import webdriver
import pytest

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


@pytest.fixture
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(options=options)  # options=options
        print("Launching Chrome browser.......")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser.......")
    else:
        driver = webdriver.Chrome(options=options)  # options=options
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks // CLI-(command line interface)
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser vlue to Setup method
    return request.config.getoption('--browser')
