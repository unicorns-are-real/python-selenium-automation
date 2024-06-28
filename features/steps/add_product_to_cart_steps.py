from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("Open product page")
def open_page(context):
    context.driver.get('https://www.target.com/p/san-francisco-bay-coffee-hawaiian-blend-2lb-32oz-whole-bean-coffee/-/A-88040037#lnk=sametab')
    sleep(30)


@then('Verify product is correct')
def verify_product(context):
    context.driver.find_element(By.XPATH, '//h1[text()="San Francisco Bay Coffee, Hawaiian Blend, 2lb (32oz) Whole Bean Coffee"]').is_displayed(), "Incorrect product"


@when('Click on add to cart button')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '[aria-label*="Add to cart for San Francisco Bay Coffee,"]').click()


@then('Check cart has individual item')
def check_cart(context):
    context.driver.find_element(By.XPATH, '//div[text()="San Francisco Bay Coffee, Hawaiian Blend, 2lb (32oz) Whole Bean Coffee"]').is_displayed(), "Coffee is not in the cart"
    print("Test case passed")
