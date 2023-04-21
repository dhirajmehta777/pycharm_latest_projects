import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

from utilities.readproperties import ReadConfig


@pytest.fixture(scope="class", autouse=True)
def setup(request,browser):
    if browser=="chrome":
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "ie":
        driver = webdriver.Ie(IEDriverManager().install())
    else:
        print("Invalid Browser Input")
    driver.implicitly_wait(10)
    driver.get(ReadConfig.getApplicationURL())
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")
