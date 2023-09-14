import pytest
from selenium import webdriver

from utilities import readconfigurations


@pytest.fixture()
def setup_and_teardown(request):
    browser = readconfigurations.read_configuration("basic info", "browser")
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Please provide a valid browser")
    driver.maximize_window()
    app_url = readconfigurations.read_configuration("basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
