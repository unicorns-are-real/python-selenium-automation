from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on cart icon')
def cart_click(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()
    sleep(10)


@then('"Your cart is empty" message is shown')
def empty_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "h1.sc-fe064f5c-0.dtCtuk").is_displayed(), 'Header "empty cart" not shown'
    print('Test case passed')
