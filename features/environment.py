from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
# explicit wait


def browser_init(context):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    context.driver.maximize_window()
    #context.driver.implicitly_wait(5) #implicit wait
    context.wait = WebDriverWait(context.driver, 15)  # explicit wait


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        #context.driver.save_screenshot(f'step_failed_{step}.png') - take screenshot of failed step
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
