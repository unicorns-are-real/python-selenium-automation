from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.XPATH, "//a[@data-test='@web/CartLink']")
HEADER = (By.CSS_SELECTOR, '[class*="UtilityHeaderWrapper"]')
HEADER_LINKS = (By.CSS_SELECTOR, '[data-test*="@web/GlobalHeader/UtilityHeader"]')

@given('Open Target.com')
def open_target_com(context):
    # open page in the browser
    context.driver.get('https://target.com/')


@when('Search for {product}')
def search_product(context, product):
    # input word to a search field
    print(product)
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    # click on search button
    context.driver.find_element(*SEARCH_ICON).click()
    sleep(10)


@when('Select a product')
def select_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[aria-label*='San Francisco Bay Coffee, Hawaiian Blend']").click()
    sleep(10)

@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(10)


@then('Header is shown')
def header_is_shown(context):
    header = context.driver.find_element(*HEADER)
    print(header)


@then('Header has {expected_amount} of links')
def header_has_links(context, expected_amount):
    header_links = context.driver.find_elements(*HEADER_LINKS)
    print(header_links)
    assert len(header_links) == int(expected_amount), f"Expected {expected_amount} links, but got {len(header_links)}"
