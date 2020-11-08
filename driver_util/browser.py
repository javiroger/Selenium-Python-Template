from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager


class Browser(object):

    def __init__(self):
        self.driver = None

    def get_browser(self, browser_name):

        if browser_name == "firefox":
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser_name == "chrome":
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browser_name == "edge":
            self.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        elif browser_name == "ie":
            self.driver = webdriver.Ie(IEDriverManager().install())
        else:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        return self.driver
