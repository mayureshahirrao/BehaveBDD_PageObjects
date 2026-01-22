import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Utilities import ConfigReader


def before_scenario(context, driver):
    if ConfigReader.read_config("basic info", "browser") == 'chrome':
        context.driver = webdriver.Chrome()
    if ConfigReader.read_config("basic info", "browser") == 'firefox':
        context.driver = webdriver.Firefox()
    if ConfigReader.read_config("basic info", "browser") == 'edge':
        context.driver = webdriver.Edge()


def after_scenario(context, driver):
    context.driver.quit()


def after_step(context, step):
    print()
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
