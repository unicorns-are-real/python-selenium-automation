from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on "Add to cart" button')
def click_on_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,
                                '[aria-label*="Add to cart for San Francisco Bay Coffee"]').click()


@when('Click "View cart & check out" in the side menu')
def click_on_view_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '[href="/cart"]')
    sleep(5)


@then('Redirect to product page')
def product_page_url(context):
    url = context.driver.current_url
    assert 'san-francisco-bay-coffee-hawaiian-blend' in url, f'Expected product page but got {url}'

