from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on Sigh in icon')
def sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@aria-label='Account, sign in']").click()


@when('Click Sign in field in the side menu')
def sign_in_field(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    sleep(5)


@then('"Sign in with password" button is present')
def sign_in_button(context):
    context.driver.find_element(By.ID, 'login').is_displayed(), 'Button "sign in with password" not displayed'
    print('Test passed')
